"""
Interview Question: How do you remove duplicate values from a dictionary, keeping only the first key seen for each unique value?

Interview Explanation:
"I iterate over `data.items()`, maintaining a `seen_values` set.
If a value is not in `seen_values`, I add it to `seen_values` and keep the key-value pair in the result dictionary."
"""

def deduplicate_dict_values(data: dict) -> dict:
    seen_values = set()
    result = {}
    for key, value in data.items():
        if value not in seen_values:
            seen_values.add(value)
            result[key] = value
    return result

if __name__ == "__main__":
    sample = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
    print("Original:", sample)
    print("Deduplicated Values (First Key Retained):", deduplicate_dict_values(sample))
