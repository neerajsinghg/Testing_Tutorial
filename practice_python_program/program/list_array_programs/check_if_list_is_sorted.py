"""
Interview Question:
Write a function to check if a given list of numbers is sorted in ascending order, descending order, or monotonic.

Interview Explanation:
In Selenium/UI and API automation testing, verifying that data displayed in a web table or returned by a REST API endpoint is sorted properly (e.g., sorting columns by price, date, or name) is one of the most frequent test assertions written by SDETs.

Key Concepts:
1. `all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))` for ascending check.
2. `all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))` for descending check.
3. Returning sorting status string or boolean.
"""


def check_list_sorted_status(arr: list) -> str:
    """
    Checks whether a list is sorted in ascending, descending, or unsorted order.
    """
    if len(arr) <= 1:
        return "Sorted Ascending"

    is_asc = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    if is_asc:
        return "Sorted Ascending"

    is_desc = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    if is_desc:
        return "Sorted Descending"

    return "Unsorted"


if __name__ == "__main__":
    list1 = [10, 20, 30, 40, 50]
    list2 = [100, 80, 60, 40, 20]
    list3 = [10, 50, 20, 80, 30]

    print(f"{list1} -> {check_list_sorted_status(list1)}")
    print(f"{list2} -> {check_list_sorted_status(list2)}")
    print(f"{list3} -> {check_list_sorted_status(list3)}")
