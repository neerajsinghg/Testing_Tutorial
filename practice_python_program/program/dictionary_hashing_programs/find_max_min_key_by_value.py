"""
Interview Question: How do you find the keys with the maximum and minimum values in a dictionary?

Interview Explanation:
"I use `max(data, key=data.get)` and `min(data, key=data.get)`.
Passing `key=data.get` evaluates key selection based on corresponding dictionary values instead of string/integer keys."
"""

def get_extreme_keys(data: dict[str, int | float]) -> tuple[str, str]:
    if not data:
        raise ValueError("Dictionary is empty")
    max_key = max(data, key=data.get)
    min_key = min(data, key=data.get)
    return max_key, min_key

if __name__ == "__main__":
    scores = {"test_login": 95, "test_payment": 40, "test_search": 80, "test_signup": 100}
    max_k, min_k = get_extreme_keys(scores)
    print("Highest Score Test:", max_k, "(", scores[max_k], ")")
    print("Lowest Score Test:", min_k, "(", scores[min_k], ")")
