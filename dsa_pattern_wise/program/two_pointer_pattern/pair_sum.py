def pair_sum(arr, targate):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==targate:
                return arr[i], arr[j]

arr = [3,2,5,2,7,8,9]
targate = 14
print(pair_sum(arr, targate))