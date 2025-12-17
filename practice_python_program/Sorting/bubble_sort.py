# Bubble Sort
# It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.

# Example

def bubblesort(list):

# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)

# Output
# When the above code is executed, it produces the following result −

# [2, 6, 11, 19, 27, 31, 45, 121]