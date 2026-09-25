"""
Interview Question: How do you validate and parse HTTP response headers in Python API automation?

Interview Explanation:
"I inspect HTTP response headers dictionary (e.g. from `requests.get().headers`), normalizing keys to lower-case.
I assert essential security and contract headers such as `Content-Type == 'application/json'`, `Cache-Control`, and `Authorization` bearer token structure."
"""

def validate_response_headers(headers: dict) -> dict:
    normalized = {k.lower(): v for k, v in headers.items()}

    content_type = normalized.get("content-type", "")
    assert "application/json" in content_type, f"Invalid Content-Type! Expected application/json, got '{content_type}'"

    return {
        "content_type": content_type,
        "server": normalized.get("server", "unknown"),
        "authorization": normalized.get("authorization", "none")
    }

if __name__ == "__main__":
    mock_headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Server": "gunicorn/20.1.0",
        "Cache-Control": "no-cache"
    }

    validated_info = validate_response_headers(mock_headers)
    print("Header Validation Summary:", validated_info)
