from dataclasses import dataclass
@dataclass
class TestResult:
    test_name: str
    passed: bool
    duration_seconds: float