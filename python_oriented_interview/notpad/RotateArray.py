def reverse(arr, left, right):
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    n = len(arr)
    k = k % n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    for num in arr:
        print(num, end=" ")
    print()
