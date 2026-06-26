numbers = [1, 2, 3, 4, 5, 6, 7, 8]
target = 8

hs = set()
for num in numbers:
    complement = target - num
    if complement in hs:
        print(f"{target} = {num} + {complement}")
        break
    else:
        hs.add(num)
