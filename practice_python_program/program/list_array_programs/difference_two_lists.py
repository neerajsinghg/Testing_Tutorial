"""
Find Elements Present in First List But Not Second (Difference)
Interview Note: Set difference (-) returns items exclusive to list1.
Time Complexity: O(n + m)
Space Complexity: O(n)
"""

def find_difference(list1: list, list2: list) -> list:
    return list(set(list1) - set(list2))

if __name__ == "__main__":
    l1, l2 = [1, 2, 3, 4], [3, 4, 5]
    print("In List 1 but not List 2:", find_difference(l1, l2))
