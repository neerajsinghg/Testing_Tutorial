"""
13. Print Prime Numbers in a Range
Interview Note: Iterates through range and uses prime validation loop with for-else structure.
Time Complexity: O(n * sqrt(n))
Space Complexity: O(1)
"""

def get_primes_in_range(start: int, end: int) -> list[int]:
    primes = []
    for number in range(max(2, start), end):
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                break
        else:
            primes.append(number)
    return primes

if __name__ == "__main__":
    print("Primes between 2 and 100:", get_primes_in_range(2, 100))
