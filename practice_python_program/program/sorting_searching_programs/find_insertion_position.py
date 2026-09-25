"""
Find Search Insertion Position
Interview Note: Scans array to find target index or index where target should be inserted to maintain order.
Time Complexity: O(n) linear scan [or O(log n) via binary search].
Space Complexity: O(1)
"""

def search_insert_position(numbers: list[int], target: int) -> int:
    position = 0
    while position < len(numbers) and numbers[position] < target:
        position += 1
    return position

if __name__ == "__main__":
    numbers = [1, 3, 5, 6]
    target = 4
    print(f"Insertion position for {target} in {numbers}:", search_insert_position(numbers, target))
