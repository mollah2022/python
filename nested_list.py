numbers = [
    [1,3,5,7,9],
    [2,4,6,8,10]
]

num1 = numbers[0][2]
num2 = numbers[1][3]

print("Num1:", num1)
print("Num2:", num2)

numbers[0][3] = 600
numbers[1][3] = 700

print(numbers)

numbers_copy = numbers.copy()

numbers_copy[0][1] = 10000

print(numbers_copy)
print(numbers)

import copy

num1 = copy.deepcopy(numbers)
num1[0][1] = 900000

print(numbers)
print(num1)

name = ["sajib"]
name.pop()
name.remove("sajib")
print(name)