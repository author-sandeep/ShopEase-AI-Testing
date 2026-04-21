# SPDX-License-Identifier: MPL-2.0
# Concept 2: Markdown Stripping Mechanics
# Author: Sandeep Dixit

import json
import pytest

def strip_markdown(text: str) -> str:
    cleaned: str = text.strip()
    
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    
    return cleaned.strip()

def test_markdown_stripper() -> None:
    dirty_payload: str = '```json\n{\n "status": "ok"\n}\n```'
    
    clean_text: str = strip_markdown(dirty_payload)
    
    assert "```" not in clean_text, "Markdown remains in text!"
    assert clean_text.startswith("{"), "JSON structure damaged!"
    assert clean_text.endswith("}"), "JSON structure damaged!"
    
    parsed = json.loads(clean_text)
    assert parsed["status"] == "ok", "Data corrupted during strip."
    
    print("PASS: Markdown safely stripped and payload rescued.")

if __name__ == "__main__":
    test_markdown_stripper()
