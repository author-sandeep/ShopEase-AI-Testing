cost = CostTracker.calculate_cost("gpt-4", usage)
if cost > 0.05:
    raise ValueError("BudgetExceededError: Request costs too much!")