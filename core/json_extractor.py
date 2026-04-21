# SPDX-License-Identifier: MPL-2.0
# Concept 1: The LLM JSON Problem - Program 1
# File: core/json_extractor.py
# Purpose: Robust JSON extraction from LLM responses with multiple fallback strategies
# Author: Sandeep Dixit

import json
import re
import logging
from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from pathlib import Path
from pydantic import BaseModel, ValidationError

from core.logger import get_logger
from core.schemas import ShopEaseAIPayload

logger = get_logger(__name__)

T = TypeVar("T", bound=BaseModel)


class JsonExtractor:
    """
    Multi-strategy JSON extractor for LLM responses.

    This class implements a cascading fallback approach to extract valid JSON
    from potentially malformed or decorated LLM outputs. It handles markdown
    code blocks, trailing commas, and common LLM response patterns.

    Attributes:
        max_extraction_attempts: Number of fallback strategies available
        extraction_log: Record of which strategy succeeded for analytics
    """

    def __init__(self) -> None:
        """Initialize the JSON extractor with default strategies."""
        self.max_extraction_attempts: int = 5
        self.extraction_log: List[Dict[str, Any]] = []
        logger.info("JsonExtractor initialized with 5 fallback strategies")

    def extract_and_validate(
            self,
            raw_response: str,
            schema_class: Type[T],
            context: Optional[Dict[str, Any]] = None
    ) -> Optional[T]:
        """
        Extract JSON from LLM response and validate against Pydantic schema.

        This method attempts multiple extraction strategies in sequence,
        stopping when valid JSON matching the schema is found.

        Args:
            raw_response: Raw string response from LLM API
            schema_class: Pydantic model class for validation
            context: Optional context for logging and debugging

        Returns:
            Validated Pydantic model instance or None if extraction fails

        Raises:
            ValueError: If raw_response is empty or None
        """
        if not raw_response or not raw_response.strip():
            logger.error("Empty response received for JSON extraction")
            raise ValueError("raw_response cannot be empty")

        context = context or {}
        extraction_strategies = [
            ("direct_json", self._extract_direct_json),
            ("markdown_fence", self._extract_from_markdown_fence),
            ("regex_object", self._extract_json_object_regex),
            ("regex_array", self._extract_json_array_regex),
            ("repair_attempt", self._repair_malformed_json),
        ]

        for strategy_name, strategy_func in extraction_strategies:
            try:
                logger.debug(
                    f"Attempting extraction strategy: {strategy_name}",
                    extra={"context": context}
                )

                extracted_data = strategy_func(raw_response)

                if extracted_data is not None:
                    validated_model = self._validate_against_schema(
                        extracted_data, schema_class, strategy_name, context
                    )

                    if validated_model is not None:
                        self._log_extraction_success(
                            strategy_name, raw_response, validated_model
                        )
                        return validated_model

            except Exception as e:
                logger.warning(
                    f"Strategy {strategy_name} failed: {str(e)}",
                    extra={"context": context}
                )
                continue

        logger.error(
            f"All extraction strategies failed for response: {raw_response[:200]}...",
            extra={"context": context}
        )
        return None

    def _extract_direct_json(self, raw_response: str) -> Optional[Union[Dict, List]]:
        """
        Attempt direct JSON parsing of the entire response.

        Args:
            raw_response: Raw string response from LLM

        Returns:
            Parsed JSON as dict or list, or None if parsing fails
        """
        cleaned_response = raw_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            return None

    def _extract_from_markdown_fence(self, raw_response: str) -> Optional[Union[Dict, List]]:
        """
        Extract JSON from markdown code blocks (```json ... ``` or ``` ... ```).

        Args:
            raw_response: Raw string response that may contain markdown

        Returns:
            Parsed JSON or None if no valid JSON found in code blocks
        """
        patterns = [
            r'```json\s*\n(.*?)\n```',
            r'```\s*\n(\{.*?\})\n```',
            r'```\s*\n(\[.*?\])\n```',
            r'```json\s*(.*?)\s*```',
            r'```\s*(\{.*?\})\s*```',
        ]

        for pattern in patterns:
            match = re.search(pattern, raw_response, re.DOTALL)
            if match:
                json_content = match.group(1).strip()
                try:
                    return json.loads(json_content)
                except json.JSONDecodeError:
                    continue

        return None

    def _extract_json_object_regex(self, raw_response: str) -> Optional[Dict]:
        """
        Extract first JSON object using regex pattern matching.

        This method handles objects with balanced braces accounting for
        nested structures and string literals containing braces.

        Args:
            raw_response: Raw string response potentially containing JSON

        Returns:
            Parsed dict or None if no valid JSON object found
        """
        json_pattern = r'\{(?:[^{}]|"(?:\\.|[^"\\])*"|\{(?:[^{}]|"(?:\\.|[^"\\])*")*\})*\}'
        match = re.search(json_pattern, raw_response, re.DOTALL)

        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass

        return None

    def _extract_json_array_regex(self, raw_response: str) -> Optional[List]:
        """
        Extract first JSON array using regex pattern matching.

        Args:
            raw_response: Raw string response potentially containing JSON array

        Returns:
            Parsed list or None if no valid JSON array found
        """
        array_pattern = r'\[(?:[^\[\]]|"(?:\\.|[^"\\])*"|\[(?:[^\[\]]|"(?:\\.|[^"\\])*")*\])*\]'
        match = re.search(array_pattern, raw_response, re.DOTALL)

        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass

        return None

    def _repair_malformed_json(self, raw_response: str) -> Optional[Union[Dict, List]]:
        """
        Attempt to repair common JSON formatting errors.

        Fixes trailing commas, missing quotes around keys, and single-quoted strings.

        Args:
            raw_response: Potentially malformed JSON string

        Returns:
            Repaired and parsed JSON or None if repair fails
        """
        extracted = self._extract_json_object_regex(raw_response)

        if extracted is None:
            extracted = self._extract_json_array_regex(raw_response)

        if extracted is None:
            match = re.search(r'[\{\[].*[\}\]]', raw_response, re.DOTALL)
            if match:
                json_candidate = match.group(0)

                json_candidate = re.sub(r',\s*}', '}', json_candidate)
                json_candidate = re.sub(r',\s*]', ']', json_candidate)

                json_candidate = re.sub(
                    r'([{,])\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:',
                    r'\1 "\2":',
                    json_candidate
                )

                json_candidate = json_candidate.replace("'", '"')

                try:
                    return json.loads(json_candidate)
                except json.JSONDecodeError:
                    pass

        return None

    def _validate_against_schema(
            self,
            data: Union[Dict, List],
            schema_class: Type[T],
            strategy_name: str,
            context: Dict[str, Any]
    ) -> Optional[T]:
        """
        Validate extracted data against Pydantic schema.

        Args:
            data: Extracted JSON data as dict or list
            schema_class: Target Pydantic model class
            strategy_name: Name of extraction strategy that produced data
            context: Logging context

        Returns:
            Validated model instance or None if validation fails
        """
        try:
            if isinstance(data, list):
                if hasattr(schema_class, '__name__') and 'List' in str(schema_class):
                    return schema_class(data)
                else:
                    logger.warning(
                        f"Expected object but got array from {strategy_name}",
                        extra={"context": context}
                    )
                    return None
            else:
                return schema_class(**data)

        except ValidationError as e:
            logger.warning(
                f"Schema validation failed for {strategy_name}: {e.errors()}",
                extra={"context": context}
            )
            return None
        except TypeError as e:
            logger.warning(
                f"Type error during validation: {e}",
                extra={"context": context}
            )
            return None

    def _log_extraction_success(
            self,
            strategy_name: str,
            raw_response: str,
            validated_model: BaseModel
    ) -> None:
        """
        Log successful extraction for analytics and debugging.

        Args:
            strategy_name: Name of successful extraction strategy
            raw_response: Original LLM response
            validated_model: Successfully validated model instance
        """
        log_entry = {
            "strategy": strategy_name,
            "response_length": len(raw_response),
            "model_type": validated_model.__class__.__name__,
            "timestamp": self._get_timestamp()
        }
        self.extraction_log.append(log_entry)

        logger.info(
            f"Successfully extracted and validated JSON using {strategy_name}",
            extra={"extraction_log": log_entry}
        )

    def _get_timestamp(self) -> str:
        """Return ISO format timestamp for logging."""
        from datetime import datetime
        return datetime.utcnow().isoformat()

    def get_extraction_stats(self) -> Dict[str, Any]:
        """
        Return statistics about extraction strategy usage.

        Returns:
            Dictionary containing strategy counts and success rates
        """
        from collections import Counter

        strategy_counts = Counter(
            entry["strategy"] for entry in self.extraction_log
        )

        return {
            "total_extractions": len(self.extraction_log),
            "strategy_distribution": dict(strategy_counts),
            "most_successful_strategy": strategy_counts.most_common(1)[0][0]
            if strategy_counts else None
        }


class ProductRecommendation(BaseModel):
    """
    Pydantic schema for product recommendation responses.

    This schema validates that LLM responses contain all required fields
    for displaying product recommendations to ShopEase customers.
    """
    name: str
    price: float
    category: str
    description: Optional[str] = None
    in_stock: bool = True
    rating: Optional[float] = None

    class Config:
        extra = "forbid"
        json_schema_extra = {
            "example": {
                "name": "Wool Blend Sweater",
                "price": 2499.00,
                "category": "Winter Wear",
                "description": "Premium wool blend for warmth and comfort",
                "in_stock": True,
                "rating": 4.5
            }
        }


class ProductListResponse(BaseModel):
    """Wrapper for list of product recommendations."""
    recommendations: List[ProductRecommendation]
    total_results: int
    query_understanding: Optional[str] = None