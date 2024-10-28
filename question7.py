def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result
original_list = [1, 2, 2, 3, 4, 4, 5]
new_list = remove_duplicates(original_list)
print(new_list)  # Output: [1, 2, 3, 4, 5]
