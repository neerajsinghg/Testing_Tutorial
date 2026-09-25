"""
Find All Unique Pairs with Target Sum
Interview Note: Uses set of sorted tuples to store all unique pairs adding up to target.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_all_pairs(numbers: list[int], target: int) -> set[tuple[int, int]]:
    seen = set()
    pairs = set()

    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.add(tuple(sorted((number, complement))))
        seen.add(number)

    return pairs

if __name__ == "__main__":
    numbers = [2, 7, 4, 5, 3, 6]
    target = 9
    print(f"All unique pairs summing to {target}:", find_all_pairs(numbers, target))
