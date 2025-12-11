# 17. Write a Python program to rotate a list to the right by n positions.

my_list = [1, 2, 3, 4, 5]
n = 2
print(my_list)
# length = len(my_list)
# right_rotated = [my_list[(i - n) % length] for i in range(length)]
# print(right_rotated)

def wright_rotate_list(lst, n):
    if n>len(lst):
      return "position is larger than the length of the list"
    else:
    #   print(lst[-n:])
    #   print(lst[:-n])
      return lst[-n:] + lst[:-n]
result = wright_rotate_list(my_list, 3)
print("wright rotate :",result)

def left_rotate_lst(lst, n):
   if n>len(lst):
      return "positionn is larger than the length of the list"
   else:
      print(lst[n:])
      return lst[n:] + lst[:n]
result1 = left_rotate_lst(my_list, 3)
print("left rotate :", result1)

