def get_sum(num):
    sum_val = 0
    while num > 0:
        digit = num % 10
        sum_val += digit * digit
        num = num // 10
    return sum_val

def is_happy(num):
    fast = num
    slow = num
    while True:
        slow = get_sum(slow)
        fast = get_sum(get_sum(fast))
        if slow == fast:
            break
    return slow == 1

num = 19
if is_happy(num):
    print("this is happy num")
else:
    print("this is not a happy num")
