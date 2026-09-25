"""
API / Element Poller with Exponential Backoff
Senior SDET Context: Polls asynchronous job status or delayed web elements with increasing delay intervals until timeout.
"""

import time
from typing import Callable, Any

def poll_until_success(
    action: Callable[[], Any],
    condition: Callable[[Any], bool],
    timeout_seconds: float = 5.0,
    initial_delay: float = 0.1,
    backoff_factor: float = 2.0
) -> Any:
    start_time = time.time()
    delay = initial_delay
    attempts = 0

    while time.time() - start_time < timeout_seconds:
        attempts += 1
        result = action()
        if condition(result):
            print(f"[Polling] Succeeded on attempt {attempts} after {time.time() - start_time:.2f}s")
            return result
        print(f"[Polling] Attempt {attempts} failed. Waiting {delay:.2f}s backoff...")
        time.sleep(delay)
        delay *= backoff_factor

    raise TimeoutError(f"Condition not met within {timeout_seconds}s timeout after {attempts} attempts.")

if __name__ == "__main__":
    poll_counter = 0

    def mock_async_api():
        global poll_counter
        poll_counter += 1
        return {"status": "COMPLETED" if poll_counter >= 3 else "IN_PROGRESS"}

    try:
        final_state = poll_until_success(
            action=mock_async_api,
            condition=lambda res: res.get("status") == "COMPLETED",
            timeout_seconds=3.0,
            initial_delay=0.1,
            backoff_factor=1.5
        )
        print("Final State:", final_state)
    except TimeoutError as e:
        print("Polling Timeout:", e)
