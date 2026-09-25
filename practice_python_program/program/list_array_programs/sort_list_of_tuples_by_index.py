"""
Interview Question:
Sort a list of tuples or dictionaries by a specific element/key index (e.g., sorting test execution records by execution time or priority).

Interview Explanation:
Sorting complex data structures using key functions (`lambda` or `operator.itemgetter`) is essential in test automation reporting framework design.

Key Concepts:
1. `sorted(iterable, key=lambda x: x[index])`.
2. Using `operator.itemgetter(index)` for higher performance.
3. Multi-key sorting (e.g. primary sort by status, secondary by duration).
"""

from operator import itemgetter


def sort_tuples_by_secondary_element(tuple_list: list, index: int, reverse: bool = False) -> list:
    """
    Sorts a list of tuples by a given index using itemgetter.
    """
    return sorted(tuple_list, key=itemgetter(index), reverse=reverse)


def sort_dicts_by_key(dict_list: list, key_name: str, reverse: bool = False) -> list:
    """
    Sorts a list of dictionaries by a specified dictionary key.
    """
    return sorted(dict_list, key=lambda x: x.get(key_name, 0), reverse=reverse)


if __name__ == "__main__":
    # Test suite results: (test_name, duration_sec, status)
    test_records = [
        ("test_login", 3.4, "PASS"),
        ("test_checkout", 12.1, "FAIL"),
        ("test_signup", 1.8, "PASS"),
        ("test_payment", 7.5, "PASS")
    ]

    sorted_by_duration = sort_tuples_by_secondary_element(test_records, index=1, reverse=True)
    print("Test Records Sorted by Duration (Descending):")
    for rec in sorted_by_duration:
        print(f"  {rec[0]}: {rec[1]}s ({rec[2]})")
