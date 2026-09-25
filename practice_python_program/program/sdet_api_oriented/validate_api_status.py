"""
Interview Question: How do you validate API HTTP status codes and response headers in Python automation test suites?

Interview Explanation:
"In API automation frameworks (e.g. using `requests` or `pytest`), I assert that `response.status_code == expected_code`
and verify response header attributes such as `Content-Type == application/json`.
I encapsulate these checks in reusable assertion helpers to raise descriptive failure messages."
"""

def validate_api_status(response: dict, expected_code: int = 200, expected_msg: str = "Success") -> bool:
    actual_code = response.get("status_code")
    actual_msg = response.get("message")

    assert actual_code == expected_code, f"Status Code mismatch! Expected: {expected_code}, Got: {actual_code}"
    assert actual_msg == expected_msg, f"Message mismatch! Expected: '{expected_msg}', Got: '{actual_msg}'"
    return True

if __name__ == "__main__":
    mock_response = {
        "status_code": 200,
        "message": "Success",
        "body": {"data": "ok"}
    }

    if validate_api_status(mock_response):
        print("API Status and Message Validation Passed!")
