s = "abcabcbb"
map_dict = {}
left = 0
maxLength = 0
startIndex = 0

for right in range(len(s)):
    ch = s[right]
    if ch in map_dict:
        left = max(left, map_dict[ch] + 1)

    map_dict[ch] = right

    if right - left + 1 > maxLength:
        maxLength = right - left + 1
        startIndex = left

result = s[startIndex : startIndex + maxLength]
print("Longest Substring =", result)
print("Length =", maxLength)
