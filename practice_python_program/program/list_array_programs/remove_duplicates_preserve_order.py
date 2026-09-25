"""
Interview Question:
Remove duplicate elements from a list while preserving the original relative order of elements.

Interview Explanation:
Using `list(set(items))` removes duplicates but loses the original order of items. Preserving order while removing duplicates is a very common interview task.

Key Concepts:
1. Standard set tracking + list iteration: O(n) time, O(n) space.
2. `dict.fromkeys(items)` in Python 3.7+ preserves key insertion order natively.
"""


def remove_duplicates_using_set(items: list) -> list:
    """
    Deduplicates list while preserving item order using set lookup.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def remove_duplicates_using_dict(items: list) -> list:
    """
    Deduplicates list while preserving item order using dict.fromkeys() trick (Python 3.7+).
    """
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    sample_list = ["chrome", "firefox", "chrome", "safari", "edge", "firefox", "chrome"]

    deduped_set = remove_duplicates_using_set(sample_list)
    deduped_dict = remove_duplicates_using_dict(sample_list)

    print(f"Original List: {sample_list}")
    print(f"Deduplicated (Set Method):  {deduped_set}")
    print(f"Deduplicated (Dict Method): {deduped_dict}")
