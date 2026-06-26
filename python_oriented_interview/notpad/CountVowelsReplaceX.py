def is_vowel(chh):
    return chh in ('a', 'e', 'i', 'o', 'u')

s = "united state of america"
count = 0
sb = []
for chh in s:
    if is_vowel(chh):
        count += 1
        sb.append('X')
    else:
        sb.append(chh)

print("".join(sb))
print(f"total number of vowels = {count}")
