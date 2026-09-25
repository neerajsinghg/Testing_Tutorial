"""
20. Find Common Elements Between Two Lists
Interview Note: Set intersection (&) provides an efficient way to find common items.
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

def find_common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print("List 1:", list1)
    print("List 2:", list2)
    print("Common Elements:", find_common_elements(list1, list2))
