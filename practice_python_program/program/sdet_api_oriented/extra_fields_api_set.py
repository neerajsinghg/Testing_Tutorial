"""
Interview Question: How do you detect unexpected extra fields in an API response payload?

Interview Explanation:
"Strict schema validation requires ensuring API endpoints do not leak internal or unannounced fields.
I compute the set difference `actual_response.keys() - expected_fields`.
Any resulting keys represent extra fields not defined in the expected contract."
"""

def find_extra_api_fields(expected_fields: set[str], actual_response: dict) -> set[str]:
    return actual_response.keys() - expected_fields

if __name__ == "__main__":
    expected = {"id", "name", "email"}
    actual = {
        "id": 101,
        "name": "Neeraj",
        "email": "test@test.com",
        "phone": "9999999999"
    }

    extra = find_extra_api_fields(expected, actual)
    print("Extra API Fields:", extra)
