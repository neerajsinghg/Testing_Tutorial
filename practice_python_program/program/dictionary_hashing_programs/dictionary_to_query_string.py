"""
Interview Question:
How do you convert a Python dictionary into a URL query parameter string and vice versa?

Interview Explanation:
In API automation (REST API testing), endpoint URLs frequently accept query parameters (e.g., `?page=1&limit=10&status=passed`).
Converting a Python dictionary into a query string using `urllib.parse.urlencode` or custom dictionary comprehension is a standard requirement for building API request URLs dynamically.

Key Concepts:
1. `urllib.parse.urlencode` handles standard URL encoding for dictionary keys and values.
2. `urllib.parse.parse_qs` or `parse_qsl` parses URL query strings back into Python dictionaries.
3. Custom implementation using list comprehension and string joining.
"""

from urllib.parse import urlencode, parse_qs


def dict_to_query_string(params: dict) -> str:
    """
    Converts a dictionary of API parameters into a URL query string.
    """
    return urlencode(params)


def query_string_to_dict(query_str: str) -> dict:
    """
    Parses a URL query string back into a Python dictionary.
    """
    parsed = parse_qs(query_str)
    # Simplify single-item lists in parsed dictionary
    return {k: v[0] if len(v) == 1 else v for k, v in parsed.items()}


if __name__ == "__main__":
    api_params = {
        "page": 1,
        "limit": 20,
        "status": "active",
        "search": "test cases & execution"
    }

    query_string = dict_to_query_string(api_params)
    print(f"Generated Query String:\n?{query_string}\n")

    reconstructed_dict = query_string_to_dict(query_string)
    print(f"Reconstructed Dictionary:\n{reconstructed_dict}")
