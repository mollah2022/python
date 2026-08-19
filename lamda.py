numbers = [1,2,3,4,5]

multiply_by_two = []

for num in numbers:
    multiply_by_two.append(num * 2)

print(multiply_by_two)


multiply_by_two = map(lambda x : x * 2, numbers)
print(multiply_by_two)
for res in multiply_by_two:
    print(res)

filter_list = filter(lambda x : x % 2 == 0, numbers)
print(filter_list)
for res in filter_list:
    print(res)

from functools import reduce
reduce_list = reduce(lambda x,y : x + y, numbers)
print(reduce_list)


x = [1, 2, 3]
y = x

print(id(x))
print(id(y))