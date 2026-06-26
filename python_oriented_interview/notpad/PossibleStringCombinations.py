def combine(str_val, result, index):
    if index == len(str_val):
        if result:
            print(result)
        return

    # Include current character
    combine(str_val, result + str_val[index], index + 1)
    
    # Exclude current character
    combine(str_val, result, index + 1)

if __name__ == "__main__":
    str_val = "ABC"
    combine(str_val, "", 0)
