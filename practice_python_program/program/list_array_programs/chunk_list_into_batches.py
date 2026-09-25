"""
Interview Question:
Write a function that divides a given list into sub-lists (chunks) of a specified maximum size K.

Interview Explanation:
In automation frameworks, splitting 1,000 test cases or API payloads into smaller batches of size 50 for parallel execution via ThreadPoolExecutor or pytest-xdist is a mandatory real-world task.

Key Concepts:
1. List slicing `items[i:i + k]`.
2. `range(0, len(items), k)` step iteration.
3. Generator approach for lazy iteration over large datasets.
"""


def chunk_list(items: list, chunk_size: int) -> list:
    """
    Splits a list into smaller sub-lists of max length chunk_size.
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def chunk_list_generator(items: list, chunk_size: int):
    """
    Yields chunks of max length chunk_size lazily via a generator.
    """
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


if __name__ == "__main__":
    test_urls = [f"https://api.example.com/item/{i}" for i in range(1, 11)]
    batch_size = 3

    chunks = chunk_list(test_urls, batch_size)

    print(f"Total URLs: {len(test_urls)} | Batch Size: {batch_size}")
    for idx, batch in enumerate(chunks, start=1):
        print(f"Batch {idx}: {batch}")
