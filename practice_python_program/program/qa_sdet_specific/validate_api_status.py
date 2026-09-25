"""
43. Validate API Response Status Code and Message
Interview Note: Uses assertions for API status verification in automated test scripts.
Time Complexity: O(1)
Space Complexity: O(1)
"""

def validate_api_response(response: dict, expected_code: int = 200, expected_msg: str = "Success") -> bool:
    assert response.get("status_code") == expected_code, f"Expected {expected_code}, got {response.get('status_code')}"
    assert response.get("message") == expected_msg, f"Expected {expected_msg}, got {response.get('message')}"
    return True

if __name__ == "__main__":
    response = {"status_code": 200, "message": "Success"}
    if validate_api_response(response):
        print("API validation passed!")
