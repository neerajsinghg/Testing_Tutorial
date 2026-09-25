"""
Interview Question:
Count the frequency of each element in a list without using Python's `collections.Counter` or built-in `.count()`.

Interview Explanation:
This tests manual hash map construction and understanding how Python dictionaries store and update key counts under the hood.

Key Concepts:
1. Dictionary `get(key, default)` method.
2. Standard loop iteration over list.
3. Time Complexity: O(n), Space Complexity: O(u) where u is unique elements.
"""


def count_element_frequencies(items: list) -> dict:
    """
    Counts frequency of elements using standard dictionary hashing manually.
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


if __name__ == "__main__":
    statuses = ["PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL", "PASS"]

    freq = count_element_frequencies(statuses)

    print(f"List: {statuses}")
    print("Element Frequencies:")
    for key, value in freq.items():
        print(f"  {key}: {value}")
