"""
Interview Question:
Given an unsorted array of size N containing elements from 1 to N, where one number is missing and one number is repeating, find both numbers.

Interview Explanation:
Identifying corrupted or sequence-broken dataset elements in sequence ranges is a classic data validation challenge.

Key Concepts:
1. Hash frequency map / counting array method: O(n) time and O(n) space.
2. Mathematical equations method (sum of elements and sum of squares of elements): O(n) time and O(1) space.
"""


def find_missing_and_repeating_freq(nums: list) -> dict:
    """
    Finds missing and repeating numbers using frequency array.
    """
    n = len(nums)
    counts = [0] * (n + 1)

    for num in nums:
        counts[num] += 1

    missing = repeating = None

    for i in range(1, n + 1):
        if counts[i] == 0:
            missing = i
        elif counts[i] == 2:
            repeating = i

    return {"missing": missing, "repeating": repeating}


if __name__ == "__main__":
    arr = [4, 3, 6, 2, 1, 1]  # 5 is missing, 1 is repeating

    res = find_missing_and_repeating_freq(arr)
    print(f"Array: {arr}")
    print(f"Repeating Number: {res['repeating']}")
    print(f"Missing Number:   {res['missing']}")
