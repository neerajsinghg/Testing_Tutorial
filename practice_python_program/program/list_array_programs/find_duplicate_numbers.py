"""
Interview Question:
Find all duplicate elements in a given list of numbers or return the first repeating element.

Interview Explanation:
In automation testing (e.g., checking for duplicate record IDs, duplicate log entries, or redundant network requests), finding duplicate elements in lists is a core data validation technique.

Key Concepts:
1. Hash Set / Hash Map approach: O(n) time and O(n) space.
2. In-place tracking (if numbers are within index bounds): O(n) time and O(1) space.
3. Preserving order of duplicates vs returning unique duplicate values.
"""


def find_all_duplicates(nums: list) -> list:
    """
    Returns a list of all duplicate elements present in the input list.
    """
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


def find_first_duplicate(nums: list):
    """
    Returns the first duplicate element encountered in left-to-right traversal.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


if __name__ == "__main__":
    test_list = [4, 3, 2, 7, 8, 2, 3, 1, 4]

    all_dups = find_all_duplicates(test_list)
    first_dup = find_first_duplicate(test_list)

    print(f"Input List: {test_list}")
    print(f"All Duplicates: {all_dups}")
    print(f"First Duplicate Encountered: {first_dup}")
