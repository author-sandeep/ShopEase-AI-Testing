class MathAPI:
    def safe_divide(self, a: float, b: float) -> float:
        try:
            return a / b
        except ZeroDivisionError:
            return 0.0