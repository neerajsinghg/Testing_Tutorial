"""
Find Union of Two Lists
Interview Note: Set union (|) merges elements from both lists removing duplicates.
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

def find_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))

if __name__ == "__main__":
    l1, l2 = [1, 2, 3], [3, 4, 5]
    print("Union:", find_union(l1, l2))
