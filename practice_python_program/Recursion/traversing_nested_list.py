# 5. Traversing a Nested List
# Recursion is ideal for working with nested data structures like lists within lists. 
def sum_nested_list(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total

my_list = [1, 2, [3, 4], [5, 6, [7, 8]]]
print(f"The sum of the nested list is: {sum_nested_list(my_list)}")
 