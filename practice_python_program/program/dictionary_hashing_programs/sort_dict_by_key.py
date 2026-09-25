"""
Interview Question: How do you sort a dictionary alphabetically by its keys?

Interview Explanation:
"I use `dict(sorted(data.items()))` or `{k: data[k] for k in sorted(data)}`.
Since Python 3.7+, standard dictionaries preserve insertion order."
"""

def sort_dictionary_by_keys(data: dict) -> dict:
    return dict(sorted(data.items()))

if __name__ == "__main__":
    raw_data = {"zebra": 1, "apple": 5, "mango": 3, "banana": 2}
    print("Original:", raw_data)
    print("Sorted by Keys:", sort_dictionary_by_keys(raw_data))
