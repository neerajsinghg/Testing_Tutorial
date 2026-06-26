numbers = [16, 17, 4, 3, 5, 2]
maxFromRight = numbers[-1]
print(f"Leaders Elements = {maxFromRight}", end="")
for i in range(len(numbers) - 2, -1, -1):
    if numbers[i] > maxFromRight:
        maxFromRight = numbers[i]
        print(f", {maxFromRight}", end="")
print()
