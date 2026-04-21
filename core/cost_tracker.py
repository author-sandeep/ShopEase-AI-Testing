# SPDX-License-Identifier: MPL-2.0
# File: core/cost_tracker.py
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class CostTracker:
    PRICING_SHEET = {
        "gpt-3.5-turbo": {"input": 0.0015, "output": 0.0020},
        "gpt-4": {"input": 0.03, "output": 0.06}
    }

    @classmethod
    def calculate_cost(cls, model: str, usage_data: Dict[str, int]) -> float:
        rates = cls.PRICING_SHEET.get(model, {"input": 0, "output": 0})
        p_tok = usage_data.get("prompt_tokens", 0)
        c_tok = usage_data.get("completion_tokens", 0)
        return round(((p_tok/1000)*rates["input"]) + ((c_tok/1000)*rates["output"]), 6)