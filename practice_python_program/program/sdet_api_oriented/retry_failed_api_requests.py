"""
Interview Question: How do you build an automated retry wrapper for transient 50x API server errors?

Interview Explanation:
"I wrap API HTTP calls in a retry loop (or use urllib3 `Retry` adapter with `requests.Session`).
If the response status code is in `[500, 502, 503, 504]`, I sleep with exponential backoff before retrying up to max attempts."
"""

import time
from typing import Callable, Any

def execute_with_retry(api_call: Callable[[], dict], max_retries: int = 3, backoff_sec: float = 0.5) -> dict:
    for attempt in range(1, max_retries + 1):
        response = api_call()
        status_code = response.get("status_code", 500)

        if status_code < 500:
            return response

        print(f"[API Retry] Attempt {attempt}/{max_retries} received HTTP {status_code}. Retrying in {backoff_sec}s...")
        time.sleep(backoff_sec)
        backoff_sec *= 2

    return response

if __name__ == "__main__":
    call_counter = 0

    def mock_flaky_api():
        global call_counter
        call_counter += 1
        if call_counter < 3:
            return {"status_code": 503, "error": "Service Unavailable"}
        return {"status_code": 200, "data": "Success"}

    res = execute_with_retry(mock_flaky_api, max_retries=3)
    print("Final API Call Result:", res)
