# 1.Find the sum of elements in a list.
lst = [8,2,9,3,7]

print(sum(lst))

def list_sum(lst):
    summ =0
    for no in lst:
        summ = summ+no
    return summ

def list_summ(lst):
    return sum(lst)

result = list_sum(lst)
print(result)

result1 = list_summ(lst)
print(result1)
