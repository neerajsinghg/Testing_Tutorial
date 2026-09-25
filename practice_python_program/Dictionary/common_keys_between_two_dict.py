# common keys between two dict
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 200,
    "c": 300,
    "d": 400
}

def common_keys(dict1, dict2):
    return set(dict1.keys()) & set(dict2.keys())

print("Common keys between dict1 and dict2:", common_keys(dict1, dict2))


common = dict1.keys() & dict2.keys()

print(common)