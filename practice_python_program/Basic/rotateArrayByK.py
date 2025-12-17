arr = [1,2,3,4,5,6,7,8]
k = 3 

#left rotate
# k %= len(arr)
# arr = arr[k:]+arr[:3]

#right rotate
k%=len(arr)
arr = arr[-k:]+arr[:-k]
print(arr)