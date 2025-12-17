# 15. Find the Power Of a Number using Iteration (Most Basic)

num, power = map(int, input("Enter the num and the power : ").split())

#print(num ** power)

# Using Simple Iteration 

output = 1 
for i in range(power):
    output = output * num 
    
print(output)
