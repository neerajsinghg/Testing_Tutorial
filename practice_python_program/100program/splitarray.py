arr = [1,2,3,4,5,6]
k=3
first_part = arr[:k]
second_part = arr[k:]
arr=second_part+first_part
print(arr)