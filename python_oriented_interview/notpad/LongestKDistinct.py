s = "eceba"
k = 2
map_dict = {}

left = 0
maxLen = 0

for right in range(len(s)):
    ch = s[right]
    map_dict[ch] = map_dict.get(ch, 0) + 1

    while len(map_dict) > k:
        leftChar = s[left]
        map_dict[leftChar] -= 1
        if map_dict[leftChar] == 0:
            del map_dict[leftChar]
        left += 1

    maxLen = max(maxLen, right - left + 1)

print("Longest Length:", maxLen)
