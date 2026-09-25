"""
Most Frequent Element in List
Interview Note: Builds frequency dictionary and extracts key with max frequency count.
Time Complexity: O(n)
Space Complexity: O(u)
"""

def most_frequent(numbers: list):
    count = {}
    for number in numbers:
        count[number] = count.get(number, 0) + 1
    return max(count, key=count.get)

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 3, 3, 4]
    print("Most Frequent Element:", most_frequent(numbers))
