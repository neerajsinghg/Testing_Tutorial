"""
Sum of Digits Using Recursion
Interview Note: Base case n == 0 returns 0, recursive step n % 10 + sum_digits(n // 10).
Time Complexity: O(log10(n))
Space Complexity: O(log10(n))
"""

def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

if __name__ == "__main__":
    number = 12345
    print(f"Sum of digits of {number}:", sum_digits(number))
