"""
Decorator Pattern for Flaky Test Auto-Retry
Senior SDET Context: Wraps test execution functions to retry failed assertions or transient network/UI exceptions automatically with delay.
"""

import time
import functools
from typing import Callable, Any

def retry_on_failure(max_retries: int = 3, delay_seconds: float = 1.0, allowed_exceptions: tuple = (AssertionError, Exception)):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_retries:
                try:
                    attempts += 1
                    return func(*args, **kwargs)
                except allowed_exceptions as e:
                    print(f"[Retry Warning] Attempt {attempts}/{max_retries} for '{func.__name__}' failed: {e}")
                    if attempts >= max_retries:
                        print(f"[Retry Error] Exceeded max retries for '{func.__name__}'")
                        raise
                    time.sleep(delay_seconds)
        return wrapper
    return decorator

# Simulation usage
call_counter = 0

@retry_on_failure(max_retries=3, delay_seconds=0.1)
def flaky_api_test():
    global call_counter
    call_counter += 1
    if call_counter < 3:
        raise ConnectionError("Transient network timeout")
    return "API 200 OK Response"

if __name__ == "__main__":
    result = flaky_api_test()
    print("Flaky test final result:", result)
