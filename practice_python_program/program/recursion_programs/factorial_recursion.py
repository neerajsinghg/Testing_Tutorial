"""
Factorial Using Recursion
Interview Note: Base case n <= 1 returns 1, recursive step n * factorial(n - 1).
Time Complexity: O(n)
Space Complexity: O(n) call stack.
"""

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = 5
    print(f"Factorial({n}):", factorial(n))
