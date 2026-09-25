"""
25. Find Most Frequent Element
Interview Note: Uses max() with key=count.get over a frequency map.
Time Complexity: O(n)
Space Complexity: O(u)
"""

def most_frequent_element(numbers: list):
    count = {}
    for number in numbers:
        count[number] = count.get(number, 0) + 1
    return max(count, key=count.get)

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 3, 3, 4]
    print("Numbers:", numbers)
    print("Most Frequent Element:", most_frequent_element(numbers))
