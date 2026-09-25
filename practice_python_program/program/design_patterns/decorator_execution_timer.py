"""
Decorator Pattern for Method Execution Timing & Logging
Senior SDET Context: Measures execution performance of test steps and automation helper methods for SLA benchmarking.
"""

import time
import functools
from typing import Callable, Any

def log_execution_time(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        print(f"[EXEC START] Running '{func.__name__}'...")
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            elapsed = time.perf_counter() - start_time
            print(f"[EXEC FINISH] '{func.__name__}' completed in {elapsed:.4f} seconds.")
    return wrapper

@log_execution_time
def simulate_heavy_automation_task():
    time.sleep(0.05)
    return "Task completed successfully"

if __name__ == "__main__":
    res = simulate_heavy_automation_task()
    print("Result:", res)
