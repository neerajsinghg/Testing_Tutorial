"""
Binary Search Algorithm
Interview Note: Requires sorted input list. Repeatedly halves search space using left, right, and mid pointers.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(numbers: list[int], target: int) -> int:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    target = 7
    index = binary_search(numbers, target)
    print(f"Index of target {target}:", index)
