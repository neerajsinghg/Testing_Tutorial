"""
Interview Question: How do you validate required payload fields in an API automation framework?

Interview Explanation:
"I iterate through a list of mandatory field names and use list comprehension `[field for field in required if field not in response]`
to collect any missing field names. If the missing list is non-empty, I log an assertion failure detailing exact omitted fields."
"""

def validate_required_fields(response: dict, required_fields: list[str]) -> list[str]:
    return [field for field in required_fields if field not in response]

if __name__ == "__main__":
    required_schema = ["id", "name", "email", "status"]
    api_response = {
        "id": 101,
        "name": "Neeraj",
        "status": "active"
    }

    missing_fields = validate_required_fields(api_response, required_schema)
    if missing_fields:
        print("Missing Required Fields:", missing_fields)
    else:
        print("All required fields are present!")
