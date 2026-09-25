"""
45. Validate Required API Fields
Interview Note: Verifies presence of all compulsory keys in API response JSON.
Time Complexity: O(r) where r is required fields count.
Space Complexity: O(m) missing fields count.
"""

def validate_required_fields(response: dict, required_fields: list[str]) -> list[str]:
    return [field for field in required_fields if field not in response]

if __name__ == "__main__":
    required = ["id", "name", "email", "status"]
    response = {
        "id": 101,
        "name": "Neeraj",
        "status": "active"
    }
    missing = validate_required_fields(response, required)
    if missing:
        print("Missing required fields:", missing)
    else:
        print("All required fields are present!")
