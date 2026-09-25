# Build a dictionary from two lists

def build_dict_from_lists(keys, values):
    if len(keys) != len(values):
        raise ValueError("Keys and values lists must have the same length.")
    return {keys[i]: values[i] for i in range(len(keys))}

keys = ["a", "b", "c"]
values = [3, 4, 5]
print(build_dict_from_lists(keys, values))

def build_dict_from_lists_zip(keys, values):
    if len(keys) != len(values):
        raise ValueError("Keys and values lists must have the same length.")
    return dict(zip(keys, values))

print(build_dict_from_lists_zip(keys, values))

def build_dict_from_lists_enumerate(keys, values):
    if len(keys) != len(values):
        raise ValueError("Keys and values lists must have the same length.")
    return {key: values[i] for i, key in enumerate(keys)}

print(build_dict_from_lists_enumerate(keys, values))
