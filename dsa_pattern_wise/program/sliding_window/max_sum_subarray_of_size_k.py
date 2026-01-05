def max_sum_subarray_of_size_k(k, arr):
    n=len(arr)
    if n<k:
        return 0

    window_sum=sum(arr[:k])
    max_sum = window_sum
    for i in range(k,n):
        window_sum=window_sum+arr[i]-arr[i-k]

        max_sum=max(max_sum,window_sum)
    return max_sum

arr = [1,4,2,10,23,3,1,0,20]
k=4
print(max_sum_subarray_of_size_k(k,arr))