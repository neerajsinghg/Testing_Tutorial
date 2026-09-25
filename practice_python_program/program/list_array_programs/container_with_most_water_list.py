"""
Interview Question:
Given n non-negative integers representing vertical lines on a 2D plane, find two lines that together with the x-axis form a container containing the most water.

Interview Explanation:
Two-pointer greedy optimization for area calculation problems.

Key Concepts:
1. `left` pointer at index 0, `right` pointer at index N-1.
2. `width = right - left`, `height = min(heights[left], heights[right])`.
3. `max_area = max(max_area, width * height)`.
4. Move the pointer pointing to the shorter line inward.
5. Time Complexity: O(n), Space Complexity: O(1).
"""


def max_water_container(heights: list) -> dict:
    """
    Finds maximum water container area using two pointers.
    """
    left, right = 0, len(heights) - 1
    max_area = 0
    best_left, best_right = 0, 0

    while left < right:
        width = right - left
        h = min(heights[left], heights[right])
        area = width * h

        if area > max_area:
            max_area = area
            best_left, best_right = left, right

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return {
        "max_area": max_area,
        "left_index": best_left,
        "right_index": best_right
    }


if __name__ == "__main__":
    line_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    res = max_water_container(line_heights)
    print(f"Line Heights: {line_heights}")
    print(f"Max Water Area: {res['max_area']} (Between indices {res['left_index']} and {res['right_index']})")
