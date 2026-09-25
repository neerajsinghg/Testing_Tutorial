"""
26. Sort Dictionary by Value
Interview Note: Uses sorted() with a lambda key `lambda x: x[1]` to order items by value.
Time Complexity: O(k log k) where k is number of keys.
Space Complexity: O(k)
"""

def sort_dict_by_value(data: dict) -> dict:
    return dict(sorted(data.items(), key=lambda x: x[1]))

if __name__ == "__main__":
    data = {"A": 50, "B": 20, "C": 80}
    print("Original:", data)
    print("Sorted by value:", sort_dict_by_value(data))
