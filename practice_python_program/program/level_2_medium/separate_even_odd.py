"""
23. Separate Even and Odd Numbers
Interview Note: Partitions numbers into two separate lists based on modulo 2 division.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def separate_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    even, odd = separate_even_odd(numbers)
    print("Even:", even)
    print("Odd:", odd)
