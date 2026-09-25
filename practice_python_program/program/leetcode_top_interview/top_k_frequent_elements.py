"""
Interview Question: How do you find the top K most frequent elements in a list in Python?

Interview Explanation:
"I build a frequency counter using `collections.Counter(numbers)`.
Then I use `heapq.nlargest(k, counter.keys(), key=counter.get)` or `Counter.most_common(k)`.
This retrieves top K frequent elements in O(n log k) time."
"""

import heapq
from collections import Counter

def top_k_frequent(numbers: list[int], k: int) -> list[int]:
    count = Counter(numbers)
    return heapq.nlargest(k, count.keys(), key=count.get)

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    k = 2
    print("Input:", nums)
    print(f"Top {k} Most Frequent Elements:", top_k_frequent(nums, k))
