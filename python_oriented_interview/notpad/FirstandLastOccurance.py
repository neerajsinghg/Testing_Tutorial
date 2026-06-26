input_str = "Hello World"
target = 'o'
firstindex = -1
lastindex = -1

# first index
for i in range(len(input_str)):
    if input_str[i] == target:
        firstindex = i
        break

# last index
for i in range(len(input_str) - 1, -1, -1):
    if input_str[i] == target:
        lastindex = i
        break

if firstindex < 0:
    print(f"Character {target} is not present in string")
else:
    print(f"first index for {target} = {firstindex}")
    print(f"last index for {target} = {lastindex}")
