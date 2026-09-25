"""
Interview Question:
Find the majority element in an array (an element that appears more than N/2 times).

Interview Explanation:
Boyer-Moore Voting Algorithm is the optimal O(n) time and O(1) auxiliary space algorithm to solve this problem.

Key Concepts:
1. Candidate tracking with count incrementing/decrementing.
2. Verification pass to confirm candidate count strictly exceeds N/2.
3. Time Complexity: O(n), Space Complexity: O(1).
"""


def find_majority_element_boyer_moore(nums: list):
    """
    Finds majority element using Boyer-Moore Majority Vote algorithm.
    """
    candidate = None
    count = 0

    # Phase 1: Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate

    return None


if __name__ == "__main__":
    sample_1 = [2, 2, 1, 1, 1, 2, 2]
    sample_2 = [1, 2, 3, 4]

    res1 = find_majority_element_boyer_moore(sample_1)
    res2 = find_majority_element_boyer_moore(sample_2)

    print(f"List 1: {sample_1} -> Majority Element: {res1}")
    print(f"List 2: {sample_2} -> Majority Element: {res2}")
