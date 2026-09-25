"""
15. Fibonacci Series
Interview Note: Uses dynamic variable swapping (a, b = b, a + b) to generate first n Fibonacci numbers.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def generate_fibonacci(n: int) -> list[int]:
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    n = 10
    print(f"First {n} Fibonacci numbers:", generate_fibonacci(n))
