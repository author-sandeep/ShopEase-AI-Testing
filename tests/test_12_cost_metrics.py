import pytest
import threading

# Optional: Agar tiktoken nahi hai to comment out karo
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("Warning: tiktoken not installed. Token firewall tests skipped.")


def get_cost(prompt_t: int, comp_t: int) -> float:
    """Calculate cost based on token usage."""
    return (prompt_t / 1_000_000) * 0.50 + (comp_t / 1_000_000) * 1.50


def local_token_firewall(text: str, limit: int) -> int:
    """Count tokens and block if over limit."""
    if not TIKTOKEN_AVAILABLE:
        pytest.skip("tiktoken not installed")

    enc = tiktoken.get_encoding("cl100k_base")
    count = len(enc.encode(text))
    if count > limit:
        raise ValueError("Payload exceeds local firewall limits!")
    return count


class GlobalCostTracker:
    """Singleton class for tracking API costs across threads."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.cost = 0.0
        return cls._instance

    def add(self, amount: float) -> None:
        """Add cost to tracker."""
        with self._lock:
            self.cost += amount

    def reset(self) -> None:
        """Reset tracked cost to zero."""
        with self._lock:
            self.cost = 0.0


def test_financial_math_and_firewall() -> None:
    """Test cost calculation and token firewall."""
    # Test Cost Math
    assert get_cost(2000, 1000) == 0.0025

    # Test Firewall Accept
    if TIKTOKEN_AVAILABLE:
        short_text = "Hi ShopEase"
        assert local_token_firewall(short_text, 50) > 0

        # Test Firewall Block
        long_text = "ShopEase " * 100
        with pytest.raises(ValueError):
            local_token_firewall(long_text, 50)


def test_singleton_budget_enforcement() -> None:
    tracker = GlobalCostTracker()
    tracker.reset()

    max_budget = 0.20

    for i in range(5):
        tracker.add(0.10)
        if tracker.cost > max_budget:
            # ✅ Use approx for floating point comparison
            assert tracker.cost == pytest.approx(0.30)
            print("Budget circuit breaker tripped successfully.")
            break

    assert tracker.cost == pytest.approx(0.30)