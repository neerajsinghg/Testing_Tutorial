"""
Find Longest Consecutive Sequence in Unsorted Array
Interview Note: Converts list to set. Only starts counting sequence length from numbers where number - 1 is not in set.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def longest_consecutive(numbers: list[int]) -> int:
    num_set = set(numbers)
    longest = 0

    for number in num_set:
        if number - 1 not in num_set:
            current = number
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

    return longest

if __name__ == "__main__":
    numbers = [100, 4, 200, 1, 3, 2]
    print("Numbers:", numbers)
    print("Longest Consecutive Sequence Length:", longest_consecutive(numbers))
