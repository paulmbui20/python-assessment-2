def print_even_value_keys(dictionary):
    for key, value in dictionary.items():
        if value % 2 == 0:
            print(key)

input_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(input_dict)  
# Output:
# a
# c
