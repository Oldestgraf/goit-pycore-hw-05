import re
from typing import Callable

def generator_numbers(text: str):
    """Create generator for return each profit from string"""
    pattern = r"\d+.\d+" # Create pattern for profit data
    matches = re.findall(pattern, text) # Collect all profits to list
    # Return each result by request
    for data in matches:
        yield float(data)

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    """Collect and sum of each result from generator"""
    profit = sum(func(text))
    return profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")