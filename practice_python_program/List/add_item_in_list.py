# 5. Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[1]=30
print(list1)

list1[2][2].append(7000)
print(list1)

for x in list1:
    if isinstance(x, list): # isinstance(object, type)
        for y in x:
            if isinstance(y, list):
                for z in y:
                    print(z)


# for items in list1:
    # if isinstance(items, list):
    #     print(items)
    # else:
    #     print(items)

def print_nested(lst):
    for item in lst:
        if isinstance(item, list):
            print_nested(item)
        else:
            print(item)
print_nested(list1)


