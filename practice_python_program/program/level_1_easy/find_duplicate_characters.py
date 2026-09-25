"""
5. Find Duplicate Characters
Interview Note: Counts character frequencies and filters those with count > 1.
Time Complexity: O(n)
Space Complexity: O(u)
"""

def find_duplicates(text: str) -> list:
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    
    return [char for char, value in count.items() if value > 1]

if __name__ == "__main__":
    text = "automation"
    print("Duplicates:", find_duplicates(text))
