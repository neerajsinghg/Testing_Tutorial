"""
Interview Question:
How do you split a large dictionary into smaller chunks (batches) of a specified size N?

Interview Explanation:
In automation testing (batch processing API payloads, batching database queries, or chunking test suite execution), you frequently need to divide large data structures into fixed-size batches.

Key Concepts:
1. Converting dictionary `.items()` into an iterator or list.
2. Slicing dictionary items in steps of batch size `N`.
3. Reconstructing small dictionaries for each batch chunk.
"""


def chunk_dictionary(data_dict: dict, chunk_size: int) -> list:
    """
    Splits a dictionary into a list of smaller dictionaries, each having at most `chunk_size` key-value pairs.
    """
    items = list(data_dict.items())
    chunks = []

    for i in range(0, len(items), chunk_size):
        chunk_dict = dict(items[i:i + chunk_size])
        chunks.append(chunk_dict)

    return chunks


if __name__ == "__main__":
    test_payload = {
        "test_01": "PASS",
        "test_02": "FAIL",
        "test_03": "PASS",
        "test_04": "SKIP",
        "test_05": "PASS",
        "test_06": "FAIL",
        "test_07": "PASS",
        "test_08": "PASS"
    }

    batch_size = 3
    batches = chunk_dictionary(test_payload, batch_size)

    print(f"Total Items: {len(test_payload)} | Chunk Size: {batch_size}")
    for idx, batch in enumerate(batches, start=1):
        print(f"Batch {idx}: {batch}")
