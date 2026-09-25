"""
Interview Question:
How do you compute summary statistics (Sum, Average, Min, Max, Median) on numeric values in a dictionary?

Interview Explanation:
When aggregating test execution metrics (e.g., test durations, API response times per endpoint, error counts per module), SDETs need to calculate summary metrics from dictionary records.

Key Concepts:
1. Extracting numeric dictionary values via `.values()`.
2. Using built-in functions `sum()`, `min()`, `max()`, and standard math calculations.
3. Returning structured result dictionaries for reporting.
"""


def calculate_dictionary_stats(metrics_dict: dict) -> dict:
    """
    Calculates numerical statistics for dictionary values.
    """
    values = [val for val in metrics_dict.values() if isinstance(val, (int, float))]

    if not values:
        return {"count": 0, "sum": 0, "avg": 0.0, "min": None, "max": None}

    total_sum = sum(values)
    count = len(values)
    average = round(total_sum / count, 2)
    minimum = min(values)
    maximum = max(values)

    return {
        "count": count,
        "sum": round(total_sum, 2),
        "avg": average,
        "min": minimum,
        "max": maximum
    }


if __name__ == "__main__":
    response_times_ms = {
        "login_api": 145.5,
        "get_user_profile": 89.2,
        "update_settings": 210.0,
        "logout_api": 65.4,
        "checkout_cart": 320.1
    }

    stats = calculate_dictionary_stats(response_times_ms)
    print("API Response Time Statistics (ms):")
    for key, value in stats.items():
        print(f"  {key}: {value}")
