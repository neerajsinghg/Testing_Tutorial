"""
Fibonacci Using Recursion
Interview Note: Base case n <= 1 returns n, recursive step fibonacci(n - 1) + fibonacci(n - 2).
Time Complexity: O(2^n)
Space Complexity: O(n) call stack depth.
"""

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 6
    print(f"Fibonacci({n}):", fibonacci(n))
