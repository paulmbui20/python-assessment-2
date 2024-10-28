def has_pair_with_sum(int_list, target_sum):
    seen_numbers = set()
    for number in int_list:
        complement = target_sum - number
        if complement in seen_numbers:
            return True
        seen_numbers.add(number)
    return False

numbers = [1, 2, 3, 4, 5]
target = 2
result = has_pair_with_sum(numbers, target)
print(result)  # Output: False

target = 5
result = has_pair_with_sum(numbers, target)
print(result)  # Output: True

