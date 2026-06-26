s = "this is my pen" # o/p- nep ym si siht
ch = list(s)
left = 0
right = len(ch) - 1
while left < right:
    temp = ch[left]
    ch[left] = ch[right]
    ch[right] = temp
    left += 1
    right -= 1

print("".join(ch))
