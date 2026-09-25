"""
Interview Question:
Find the equilibrium index of a list. An equilibrium index is an index such that the sum of elements at lower indices is equal to the sum of elements at higher indices.

Interview Explanation:
Efficiently computing prefix and suffix sums without re-calculating sub-array totals repeatedly is a fundamental algorithm optimization.

Key Concepts:
1. `total_sum = sum(nums)`.
2. Maintain running `left_sum`.
3. `right_sum = total_sum - left_sum - num`.
4. Time Complexity: O(n) single pass, Space Complexity: O(1).
"""


def find_equilibrium_index(nums: list) -> int:
    """
    Returns the first equilibrium index in the list, or -1 if no such index exists.
    """
    total_sum = sum(nums)
    left_sum = 0

    for idx, num in enumerate(nums):
        right_sum = total_sum - left_sum - num

        if left_sum == right_sum:
            return idx

        left_sum += num

    return -1


if __name__ == "__main__":
    sample_list = [-7, 1, 5, 2, -4, 3, 0]

    eq_idx = find_equilibrium_index(sample_list)

    print(f"List: {sample_list}")
    if eq_idx != -1:
        left_part = sample_list[:eq_idx]
        right_part = sample_list[eq_idx + 1:]
        print(f"Equilibrium Index: {eq_idx} (Value: {sample_list[eq_idx]})")
        print(f"Left Sublist: {left_part} (Sum: {sum(left_part)})")
        print(f"Right Sublist: {right_part} (Sum: {sum(right_part)})")
    else:
        print("No equilibrium index found.")
