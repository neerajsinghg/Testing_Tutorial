"""
19. Two Sum Problem
Interview Note: Key hash-map problem. For each element, checks if target - number is in hash map.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return (seen[complement], index)
        seen[number] = index
    return None

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum(numbers, target)
    print(f"Indices for target {target}:", result)
