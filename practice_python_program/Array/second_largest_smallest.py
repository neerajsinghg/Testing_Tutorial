nums = [2, 4, 7, 3, 1, 9, 8]
#8
first = second_smllest = float('inf')
largest = second_largest = float('-inf')
for x in nums:
    
# Smallest logic
    if x < first:
        second_smllest = first
        first = x #2
    elif x < second_smllest and x != first:
        second_smllest = x #4
# Largest logic
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        second_largest = x

print("Second Smallest:", second_smllest)
print("Second Largest:", second_largest)
print("Smallest:", first)
print("Largest:", largest)