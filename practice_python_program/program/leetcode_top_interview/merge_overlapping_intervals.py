"""
Interview Question: How do you merge overlapping intervals in a list of time/range pairs in Python?

Interview Explanation:
"I first sort intervals by start time `intervals.sort(key=lambda x: x[0])`.
I initialize `merged = [intervals[0]]`. For each subsequent interval, if its start time <= `merged[-1][1]` (the last merged interval's end time),
I merge them by updating `merged[-1][1] = max(merged[-1][1], interval[1])`. Otherwise, I append the interval. Time complexity is O(n log n)."
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged

if __name__ == "__main__":
    sample_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Original Intervals:", sample_intervals)
    print("Merged Intervals:", merge_intervals(sample_intervals))
