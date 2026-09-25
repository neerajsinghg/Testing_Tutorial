"""
`zip()` Function Usage
Interview Question: How do you combine parallel lists into tuples or a dictionary?
Explanation: `zip(iter1, iter2)` pairs corresponding elements from multiple iterables until the shortest iterable exhausts.
"""

def combine_names_and_scores(names: list[str], scores: list[int]) -> dict[str, int]:
    return dict(zip(names, scores))

if __name__ == "__main__":
    names = ["Amit", "Neeraj", "Rahul"]
    scores = [80, 90, 85]
    print("Zipped Dict:", combine_names_and_scores(names, scores))
