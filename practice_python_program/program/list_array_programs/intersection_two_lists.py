"""
Find Intersection of Two Lists
Interview Note: Set intersection (&) finds common elements present in both collections.
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

def find_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    l1, l2 = [1, 2, 3, 4], [3, 4, 5, 6]
    print("Intersection:", find_intersection(l1, l2))
