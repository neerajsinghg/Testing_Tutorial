"""
Interview Question: How do you identify missing mandatory fields from an API JSON response in Python?

Interview Explanation:
"I define a set of expected mandatory field names `expected_fields = {'id', 'name', 'email', 'status'}`.
I convert the keys of the actual API response into a set using `actual_response.keys()`.
Using set difference `expected_fields - actual_response.keys()`, I compute missing keys in O(1) average lookup time per key."
"""

def find_missing_api_fields(expected_fields: set[str], actual_response: dict) -> set[str]:
    return expected_fields - actual_response.keys()

if __name__ == "__main__":
    expected = {"id", "name", "email", "status"}
    actual = {
        "id": 101,
        "name": "Neeraj",
        "status": "active"
    }

    missing = find_missing_api_fields(expected, actual)
    print("Missing API Fields:", missing)
