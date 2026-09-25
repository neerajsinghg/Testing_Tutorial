"""
14. Factorial of a Number
Interview Note: Computes product of all positive integers <= n.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def calculate_factorial(n: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    n = 5
    print(f"Factorial of {n}:", calculate_factorial(n))
