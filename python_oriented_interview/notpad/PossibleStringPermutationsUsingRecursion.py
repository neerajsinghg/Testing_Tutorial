def permute(str_val, result):
    if len(str_val) == 0:
        print(result)
        return

    for i in range(len(str_val)):
        current = str_val[i]
        remaining = str_val[:i] + str_val[i+1:]
        permute(remaining, result + current)

if __name__ == "__main__":
    str_val = "ABC"
    permute(str_val, "")
