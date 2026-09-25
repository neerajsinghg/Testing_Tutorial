"""
Invert a Dictionary (Swap Keys and Values)
Interview Note: Uses dictionary comprehension `{value: key for key, value in data.items()}`.
Time Complexity: O(k)
Space Complexity: O(k)
"""

def invert_dict(data: dict) -> dict:
    return {value: key for key, value in data.items()}

if __name__ == "__main__":
    data = {"a": 1, "b": 2, "c": 3}
    print("Inverted Dict:", invert_dict(data))
