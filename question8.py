def keys_greater_than_n(input_dict, n):
    result = []
    for key, value in input_dict.items():
        if value > n:
            result.append(key)
    return result

example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
keys_list = keys_greater_than_n(example_dict, n)
print(keys_list)  # Output: ['a', 'b']

