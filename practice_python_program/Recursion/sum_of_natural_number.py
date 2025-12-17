# 3. Sum of Natural Numbers
# This function calculates the sum of all natural numbers up to a given number n. 

def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

num = 4
print(f"The sum of natural numbers up to {num} is {sum_natural_numbers(num)}")
 