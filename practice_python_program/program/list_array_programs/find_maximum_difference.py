"""
Find Maximum Difference (Best Time to Buy and Sell Stock)
Interview Note: Tracks minimum value seen so far and computes max difference in single pass.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_difference(numbers: list[int | float]) -> int | float:
    if not numbers:
        return 0
    minimum = numbers[0]
    max_diff = 0
    for number in numbers:
        minimum = min(minimum, number)
        max_diff = max(max_diff, number - minimum)
    return max_diff

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Stock Prices:", prices)
    print("Max Difference/Profit:", max_difference(prices))
