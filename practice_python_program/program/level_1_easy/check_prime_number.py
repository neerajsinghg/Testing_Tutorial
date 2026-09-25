"""
12. Check Whether a Number is Prime
Interview Note: A prime number is > 1 with no divisors other than 1 and itself. Checking up to sqrt(n) optimizes trial division.
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = 17
    print(f"Is {n} prime?", is_prime(n))
