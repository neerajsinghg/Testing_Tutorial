"""
Bubble Sort Algorithm
Interview Note: Repeatedly swaps adjacent out-of-order elements until array is sorted.
Time Complexity: O(n^2) worst/average, O(n) best if optimized.
Space Complexity: O(1) in-place.
"""

def bubble_sort(numbers: list[int | float]) -> list[int | float]:
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers

if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 2]
    print("Original:", numbers)
    print("Bubble Sorted:", bubble_sort(numbers.copy()))
