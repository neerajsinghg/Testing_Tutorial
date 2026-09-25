"""
Interview Question: How do you find the two vertical lines that form a container storing the most water (Container With Most Water)?

Interview Explanation:
"I use two pointers starting at opposite ends of the array (`left = 0`, `right = len(height) - 1`).
The area is `(right - left) * min(height[left], height[right])`. In each step, I update max_area and move the pointer with the shorter height inward,
since moving the taller pointer could never increase the area. This computes max water in O(n) time and O(1) space."
"""

def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    maximum_area = 0

    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        maximum_area = max(maximum_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum_area

if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Heights:", heights)
    print("Maximum Water Area:", max_area(heights))
