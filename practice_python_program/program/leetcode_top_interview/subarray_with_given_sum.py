"""
Interview Question: How do you find a contiguous subarray with a given sum in a non-negative integer array?

Interview Explanation:
"I use a sliding window with two pointers (`left` and `right`).
I expand the window by adding `numbers[right]` to `current_sum`. While `current_sum > target` and `left <= right`,
I shrink the window from the left. If `current_sum == target`, I return the `(left, right)` indices.
This achieves O(n) time and O(1) space."
"""

def find_subarray_with_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    current_sum = 0

    for right in range(len(numbers)):
        current_sum += numbers[right]
        while current_sum > target and left < right:
            current_sum -= numbers[left]
            left += 1

        if current_sum == target:
            return (left, right)

    return None

if __name__ == "__main__":
    numbers = [1, 4, 20, 3, 10, 5]
    target = 33
    result = find_subarray_with_sum(numbers, target)
    print(f"Subarray indices summing to {target}:", result)
    if result:
        l, r = result
        print(f"Subarray slice: {numbers[l:r+1]}")
