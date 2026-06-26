# First method: Two pointer with set logic
def method_1(s):
    left = 0
    right = 0
    maxLength = 0
    char_set = set()

    while right < len(s):
        ch = s[right]
        if ch not in char_set:
            char_set.add(ch)
            maxLength = max(maxLength, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1

    print("Longest Length =", maxLength)

# Second method: Sliding window logic
def method_2(s):
    char_set = set()
    left = 0
    maxLen = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        maxLen = max(maxLen, right - left + 1)

    print("Longest substring length:", maxLen)

if __name__ == "__main__":
    s = "abcabcbb"
    method_1(s)
    method_2(s)
