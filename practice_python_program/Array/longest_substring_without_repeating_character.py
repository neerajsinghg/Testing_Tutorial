# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

def longest_substring(s):
    char_index_map = {}
    start = 0
    max_len = 0

    for idx, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = idx
        max_len = max(max_len, idx - start + 1)

    return max_len

s = "abcabcbb"
print(longest_substring(s))

# another aproche
def longest_substring_simple(s):
    # Agar string empty hai toh 0 return karo
    if not s:
        return 0
    
    max_len = 0
    
    # Har character se start karke dekhte hain
    for i in range(len(s)):
        # Ek set banayenge jo track karega ki konsa character already dekha hai
        seen = set()
        current_len = 0
        
        # i se shuru karke aage badhte hain
        for j in range(i, len(s)):
            # Agar character pehle se seen hai, toh break karo
            if s[j] in seen:
                break
            # Nahi toh set mein add karo
            seen.add(s[j])
            current_len += 1
        
        # Check karo kya yeh sabse lambha substring hai
        if current_len > max_len:
            max_len = current_len
    
    return max_len

# Test karte hain
s = "abcabcbb"
print(longest_substring_simple(s))  # Output: 3