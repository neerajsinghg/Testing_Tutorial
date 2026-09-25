"""
Interview Question:
Merge two sorted lists into a single sorted list without using Python's built-in `.sort()` or `sorted()` functions.

Interview Explanation:
This tests your understanding of the two-pointer technique and basic algorithmic sorting mechanics (part of Merge Sort).

Key Concepts:
1. Two Pointers (`i` and `j`) tracking current position in each sorted list.
2. Comparing elements at current pointers and appending the smaller one to the merged result.
3. Appending remaining items when one pointer reaches the end of its list.
4. Time Complexity: O(n + m), Space Complexity: O(n + m).
"""


def merge_two_sorted_lists(list1: list, list2: list) -> list:
    """
    Merges two sorted lists into a single sorted list in O(n + m) time.
    """
    i, j = 0, 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append remaining elements from either list
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


if __name__ == "__main__":
    arr1 = [1, 3, 5, 8, 12]
    arr2 = [2, 4, 6, 7, 9, 10, 15]

    result = merge_two_sorted_lists(arr1, arr2)
    print(f"List 1: {arr1}")
    print(f"List 2: {arr2}")
    print(f"Merged Sorted List: {result}")
