data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

# Find duplicate values
def find_duplicate_values(data):
    duplicate_values = []
    for key, value in data.items():
        if list(data.values()).count(value) > 1 and value not in duplicate_values:
            duplicate_values.append(value)
    return duplicate_values

duplicate_values = find_duplicate_values(data)  
print("Duplicate values:", duplicate_values)

def find_duplicate_values1(data):
    value_count = {}
    for value in data.values():
        value_count[value] = value_count.get(value, 0) + 1
    duplicate_values = [value for value, count in value_count.items() if count > 1]
    return duplicate_values

duplicate_values1 = find_duplicate_values1(data)
print("Duplicate values (method 2):", duplicate_values1)
