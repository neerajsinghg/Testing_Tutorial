"""
`enumerate()` Function Usage
Interview Question: How do you track item index while iterating through a loop?
Explanation: `enumerate(iterable, start=0)` yields (index, item) pairs, avoiding manual counter increments.
"""

def print_indexed_items(items: list[str], start_index: int = 1):
    output = []
    for index, name in enumerate(items, start=start_index):
        output.append(f"{index}: {name}")
    return output

if __name__ == "__main__":
    names = ["Amit", "Neeraj", "Rahul"]
    print("Enumerated items:")
    for line in print_indexed_items(names, start_index=1):
        print(line)
