def find_largest_number(num_tuple):
    largest = num_tuple[0]  # Start by assuming the first number is the largest
    for num in num_tuple:
        if num > largest:
            largest = num
    return largest

numbers = (10, 20, 30, 40, 50)
largest_number = find_largest_number(numbers)
print(largest_number)  # Output: 50
