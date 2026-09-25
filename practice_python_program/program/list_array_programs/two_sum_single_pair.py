"""
Find Pair Whose Sum Equals Target
Interview Note: Uses a set for O(1) complement lookup to return the first pair adding up to target.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_target_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    return None

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print("Pair:", find_target_pair(numbers, target))
