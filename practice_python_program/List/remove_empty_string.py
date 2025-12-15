# 11. Remove empty strings from the list of strings without using any loops

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 =[]
for word in list1:
    if word !="":
        list2.append(word)
print(list2)

list3=[]
for word in list1:
    if word =="":
        continue
    list3.append(word)
print(list3)