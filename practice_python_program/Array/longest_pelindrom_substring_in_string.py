def longest_palindrome(s):
    if not s:  # agar string khali hai
        return ""
    
    result = ""  # final answer store karenge
    
    for i in range(len(s)):
        # Case 1: Odd length palindrome (center i pe)
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Agar current palindrome result se bada hai
            if (r - l + 1) > len(result):
                result = s[l:r+1]
            l -= 1  # left ko expand karo
            r += 1  # right ko expand karo
        
        # Case 2: Even length palindrome (center i aur i+1 ke beech)
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(result):
                result = s[l:r+1]
            l -= 1
            r += 1
    
    return result

# Test karte hain
test_cases = ["mississippi", "avcccvbgf", "abcdc", "a", "abc"]

for s in test_cases:
    print(f"String: {s} -> Longest Palindrome: {longest_palindrome(s)}")