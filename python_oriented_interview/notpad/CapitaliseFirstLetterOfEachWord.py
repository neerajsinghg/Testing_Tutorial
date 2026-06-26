s = "this is my pen"
words = s.split(" ")
sb = []
for word in words:
    if word:
        sb.append(word[0].upper() + word[1:])
    else:
        sb.append("")

print(" ".join(sb).strip())
