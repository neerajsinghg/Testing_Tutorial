"""
Lazy-Loading Generator for Large Test Datasets
Senior SDET Context: Uses `yield` to stream large CSV or JSON data iteratively without loading massive files entirely into memory.
"""

from typing import Generator

def stream_user_test_data(total_records: int = 5) -> Generator[dict, None, None]:
    for i in range(1, total_records + 1):
        yield {
            "user_id": 1000 + i,
            "email": f"user_{i}@automation.com",
            "role": "QA" if i % 2 == 0 else "Admin"
        }

if __name__ == "__main__":
    print("Streaming data iteratively:")
    for user_record in stream_user_test_data(5):
        print("Processing test record:", user_record)
