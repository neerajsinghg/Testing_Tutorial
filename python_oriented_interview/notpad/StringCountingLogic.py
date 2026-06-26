input_str = "aaabbc" # output="a3b2c1"
sb = []
count = 1

for i in range(1, len(input_str) + 1):
    if i < len(input_str) and input_str[i] == input_str[i - 1]:
        count += 1
    else:
        sb.append(f"{input_str[i - 1]}{count}")
        count = 1

print("".join(sb))
