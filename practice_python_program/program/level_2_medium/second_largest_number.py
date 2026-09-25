"""
16. Find Second-Largest Number
Interview Note: Shows both sorting approach O(n log n) and single-pass optimal approach O(n).
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_second_largest_single_pass(numbers: list[int | float]) -> int | float:
    largest = float("-inf")
    second = float("-inf")

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif largest > number > second:
            second = number

    return second

if __name__ == "__main__":
    numbers = [10, 50, 20, 90, 70]
    print("Numbers:", numbers)
    print("Second Largest:", find_second_largest_single_pass(numbers))
