"""
Interview Question: How do you find all duplicate numbers in an array where elements are 1 <= nums[i] <= n in O(n) time and O(1) space?

Interview Explanation:
"Since elements are in the range 1..n, I can use the array itself as a hash table by mapping values to indices `index = abs(num) - 1`.
If `numbers[index]` is negative, I've seen `abs(num)` before, so I append it to duplicates. Otherwise, I negate `numbers[index]` to mark it as visited."
"""

def find_duplicates_in_place(numbers: list[int]) -> list[int]:
    duplicates = []
    for num in numbers:
        index = abs(num) - 1
        if numbers[index] < 0:
            duplicates.append(abs(num))
        else:
            numbers[index] = -numbers[index]
    return duplicates

if __name__ == "__main__":
    numbers = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Original:", [4, 3, 2, 7, 8, 2, 3, 1])
    print("Duplicates found in-place:", find_duplicates_in_place(numbers))
