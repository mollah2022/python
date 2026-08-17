numbers = [1,2,3,4,5,6]

new_list = [] 

for num in numbers:
    new_list.append(num * num)

print(new_list)

another_new_list = [ num*2 for num in numbers]
print(another_new_list)

numbers = [10, 20, 30]

result = [str(number) for number in numbers]

print(result)


name = ["sajib","rakib","tamim","nasir"]

new_name_list = [ nam.upper() for nam in name]

print(new_name_list)

numbers = [1,2,3,4,5,6,7,8,9,10]

even_number = [ num for num in numbers if num % 2 == 0 ]
print(even_number)


value = [
    [1,3,5,7,9],
    [2,4,6,8,10]
]

result = [ num for val in value for num in val]
print(result)