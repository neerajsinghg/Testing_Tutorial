"""
Interview Question: How do you compare expected vs actual API JSON responses and report field mismatches in Python?

Interview Explanation:
"I iterate through expected key-value pairs and compare them against the actual response dictionary using `actual.get(key)`.
If a key is missing or values do not match, I record a structured mismatch dict containing `{key: {'expected': expected_val, 'actual': actual_val}}`.
This allows detailed test reporting in automation logs and assertion reports."
"""

def compare_api_responses(expected: dict, actual: dict) -> dict:
    mismatches = {}
    for key, expected_value in expected.items():
        actual_value = actual.get(key)
        if expected_value != actual_value:
            mismatches[key] = {
                "expected": expected_value,
                "actual": actual_value
            }
    return mismatches

if __name__ == "__main__":
    expected_response = {
        "status": "success",
        "count": 10,
        "message": "Success"
    }

    actual_response = {
        "status": "success",
        "count": 8,
        "message": "Success"
    }

    diffs = compare_api_responses(expected_response, actual_response)
    print("API Response Comparison Result:")
    if diffs:
        for field, details in diffs.items():
            print(f" - {field}: Expected={details['expected']}, Actual={details['actual']}")
    else:
        print("All API response fields match expected contract!")
