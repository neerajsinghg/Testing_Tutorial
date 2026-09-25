"""
35. Flatten a Nested List
Interview Note: Uses recursion and isinstance(item, list) to unpack arbitrary nesting depths.
Time Complexity: O(N) where N total number of elements.
Space Complexity: O(D) recursion stack depth.
"""

def flatten_list(data: list) -> list:
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    data = [1, [2, 3], [4, [5, 6]]]
    print("Nested List:", data)
    print("Flattened List:", flatten_list(data))
