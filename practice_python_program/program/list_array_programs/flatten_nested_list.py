"""
Interview Question:
Write a function to flatten an arbitrarily nested list into a flat single-level list.

Interview Explanation:
Nested data structures (e.g. JSON test suites, tree nodes, or multi-level execution tags) often need to be unrolled/flattened. Recursion vs iterative stack approaches are tested here.

Key Concepts:
1. Recursive traversal checking `isinstance(item, list)`.
2. Iterative approach using stack data structure.
"""


def flatten_list_recursive(nested: list) -> list:
    """
    Recursively flattens an arbitrarily nested list structure.
    """
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list_recursive(item))
        else:
            flat.append(item)
    return flat


def flatten_list_iterative(nested: list) -> list:
    """
    Iteratively flattens a nested list using a stack.
    """
    stack = list(nested)
    flat = []
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack
        else:
            flat.append(item)
    return flat


if __name__ == "__main__":
    nested_data = [1, [2, [3, 4], 5], 6, [7, [8, [9]]]]

    flattened_rec = flatten_list_recursive(nested_data)
    flattened_iter = flatten_list_iterative(nested_data)

    print(f"Nested List: {nested_data}")
    print(f"Flattened (Recursive): {flattened_rec}")
    print(f"Flattened (Iterative): {flattened_iter}")
