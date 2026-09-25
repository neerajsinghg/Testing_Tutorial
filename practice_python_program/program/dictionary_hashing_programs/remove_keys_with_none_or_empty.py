"""
Interview Question: How do you sanitize an API payload dictionary by removing keys with None or empty values?

Interview Explanation:
"I use dictionary comprehension `{k: v for k, v in data.items() if v is not None and v != '' and v != []}`
to clean payload parameters before making HTTP POST/PUT API requests."
"""

def sanitize_payload(payload: dict) -> dict:
    return {k: v for k, v in payload.items() if v is not None and v != "" and v != []}

if __name__ == "__main__":
    raw_payload = {
        "user_id": 101,
        "name": "Neeraj",
        "email": None,
        "address": "",
        "roles": ["QA"],
        "preferences": []
    }
    print("Raw Payload:", raw_payload)
    print("Sanitized Payload:", sanitize_payload(raw_payload))
