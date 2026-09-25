"""
Interview Question: How do you pivot/swap outer and inner keys of a 2D nested dictionary in Python?

Interview Explanation:
"I iterate through outer keys `outer_key` and inner dictionaries `inner_dict`.
For each `inner_key, val` pair, I set `result[inner_key][outer_key] = val` using `collections.defaultdict(dict)`."
"""

from collections import defaultdict

def pivot_nested_dict(nested_data: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    pivoted = defaultdict(dict)
    for outer_key, inner_map in nested_data.items():
        for inner_key, val in inner_map.items():
            pivoted[inner_key][outer_key] = val
    return {k: dict(v) for k, v in pivoted.items()}

if __name__ == "__main__":
    matrix = {
        "AuthSuite": {"Chrome": 10, "Firefox": 12},
        "SearchSuite": {"Chrome": 15, "Firefox": 18}
    }
    print("Original Matrix:", matrix)
    print("Pivoted (Env -> Suite):", pivot_nested_dict(matrix))
