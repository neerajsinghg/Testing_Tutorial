"""
Product of Array Except Self
Interview Note: Demonstrates both naive O(n^2) approach and prefix/suffix product optimal O(n) approach.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def product_except_self(numbers: list[int]) -> list[int]:
    n = len(numbers)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= numbers[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= numbers[i]

    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print("Numbers:", numbers)
    print("Product except self:", product_except_self(numbers))
