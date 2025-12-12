# Find the Missing Number in an Array
# Find the missing number in an array containing ndistinct numbers from 0 to n.

def missing_number(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = [3, 0, 1]
print(missing_number(arr))

arr1 = [4,6, 1, 2]
arr1.sort()
missing_num = []
for i in range(1, len(arr1)-1):
    if arr1[i+1] != arr1[i]+1:
        print(arr1[i]+1)

