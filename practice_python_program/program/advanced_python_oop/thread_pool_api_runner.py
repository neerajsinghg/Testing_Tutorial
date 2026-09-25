"""
Parallel API Execution Runner using ThreadPoolExecutor
Senior SDET Context: Runs multiple API endpoint checks concurrently to drastically reduce regression execution times.
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def execute_api_health_check(endpoint: str) -> dict:
    start_time = time.perf_counter()
    time.sleep(0.05)
    elapsed = time.perf_counter() - start_time
    return {
        "endpoint": endpoint,
        "status_code": 200,
        "latency_ms": round(elapsed * 1000, 2)
    }

def run_api_suite_parallel(endpoints: list[str], max_workers: int = 3) -> list[dict]:
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(execute_api_health_check, url): url for url in endpoints}
        for future in as_completed(future_to_url):
            try:
                data = future.result()
                results.append(data)
            except Exception as exc:
                print(f"Endpoint {future_to_url[future]} generated an exception: {exc}")
    return results

if __name__ == "__main__":
    urls = [
        "https://api.example.com/v1/users",
        "https://api.example.com/v1/orders",
        "https://api.example.com/v1/payments",
        "https://api.example.com/v1/health"
    ]
    print("Running Parallel API Suite...")
    summary = run_api_suite_parallel(urls, max_workers=4)
    for res in summary:
        print("Result:", res)
