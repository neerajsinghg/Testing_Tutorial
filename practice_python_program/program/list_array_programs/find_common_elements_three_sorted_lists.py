"""
Interview Question:
Given three sorted lists, find all common elements present in all three lists without extra space.

Interview Explanation:
Three-pointer comparison across three sorted arrays is a classic SDET problem to test optimal index synchronization without set intersections.

Key Concepts:
1. Three pointers (`i`, `j`, `k`).
2. If elements at all 3 pointers are equal, record element and advance all 3 pointers.
3. Otherwise, advance pointer with the smallest value.
4. Time Complexity: O(n1 + n2 + n3), Space Complexity: O(1).
"""


def find_common_in_three_sorted(arr1: list, arr2: list, arr3: list) -> list:
    """
    Finds common elements across three sorted lists in O(N) time and O(1) space.
    """
    i = j = k = 0
    common = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            # Avoid duplicate recordings if same common element repeats
            if not common or common[-1] != arr1[i]:
                common.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common


if __name__ == "__main__":
    l1 = [1, 5, 10, 20, 40, 80]
    l2 = [6, 7, 20, 80, 100]
    l3 = [3, 4, 15, 20, 30, 70, 80, 120]

    result = find_common_in_three_sorted(l1, l2, l3)
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    print(f"List 3: {l3}")
    print(f"Common Elements in All Three: {result}")
