str_val = "United state of america"
arr = list(str_val)
start = 0
end = len(str_val) - 1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1

print("".join(arr))
