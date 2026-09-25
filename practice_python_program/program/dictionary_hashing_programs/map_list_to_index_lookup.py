"""
Interview Question: How do you build bidirectional value <-> index lookup dictionaries from a list in Python?

Interview Explanation:
"I use `enumerate()`: `value_to_index = {val: idx for idx, val in enumerate(items)}`
and `index_to_value = {idx: val for idx, val in enumerate(items)}`.
This allows O(1) bidirectional lookup mapping between list positions and values."
"""

def create_bidirectional_lookups(items: list) -> tuple[dict, dict]:
    val_to_idx = {val: idx for idx, val in enumerate(items)}
    idx_to_val = {idx: val for idx, val in enumerate(items)}
    return val_to_idx, idx_to_val

if __name__ == "__main__":
    elements = ["chrome", "firefox", "edge", "safari"]
    val_map, idx_map = create_bidirectional_lookups(elements)
    print("Value -> Index Map:", val_map)
    print("Index -> Value Map:", idx_map)
