numbers = (1,2,3,4,5,6,7,8)

convert_list = list(numbers)

convert_list.append(100)

numbers = tuple(convert_list)

print(numbers)