# SPDX-License-Identifier: MPL-2.0
# Concept 4: Custom Semantic Assertion - Lab Integration
# File: core/semantic_assert.py
# Purpose: Centralized vector comparison for enterprise AI testing.
# Author: Sandeep Dixit

import math
import sys
import os
from typing import List, Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("ERROR: sentence-transformers required.")
    SentenceTransformer = None

class LocalEmbedder:
    """Singleton embedding model loader."""
    _instance = None
    _model = None

    def __new__(cls, model_name: str = "all-MiniLM-L6-v2"):
        if cls._instance is None:
            cls._instance = super(LocalEmbedder, cls).__new__(cls)
            if SentenceTransformer:
                cls._model = SentenceTransformer(model_name)
        return cls._instance

    def encode(self, text: str) -> List[float]:
        """Convert text to vector."""
        if self._model is None:
            raise RuntimeError("Embedding model unavailable.")
        if not text.strip():
            dim = self._model.get_sentence_embedding_dimension()
            return [0.0] * dim
        return self._model.encode(text).tolist()

def calculate_cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Computes angular distance between two vectors."""
    try:
        if len(vec_a) != len(vec_b):
            raise ValueError("Dimension mismatch.")
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        mag_a = math.sqrt(sum(a * a for a in vec_a))
        mag_b = math.sqrt(sum(b * b for b in vec_b))
        if mag_a == 0.0 or mag_b == 0.0:
            return 0.0
        score = dot / (mag_a * mag_b)
        return max(-1.0, min(1.0, score))
    except Exception as e:
        raise e
    finally:
        pass

def assert_semantically_close(
        actual_text: str,
        expected_text: str,
        threshold: float = 0.75
) -> None:
    """
    Pytest helper to validate semantic alignment.
    Raises AssertionError if similarity < threshold.
    """
    try:
        if not actual_text or not expected_text:
            raise ValueError("Strings cannot be empty.")

        embedder = LocalEmbedder()
        vec_act = embedder.encode(actual_text)
        vec_exp = embedder.encode(expected_text)
        score = calculate_cosine_similarity(vec_act, vec_exp)

        if score < threshold:
            raise AssertionError(
                f"Mismatch. Score: {score:.4f} < {threshold}\n"
                f"Expected: '{expected_text}'\nActual: '{actual_text}'"
            )
    except AssertionError as ae:
        raise ae
    except Exception as e:
        raise RuntimeError(f"Assertion execution failed: {e}")
    finally:
        pass