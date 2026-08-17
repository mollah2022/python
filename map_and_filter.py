"""
Map : I want to change every item.
"""

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x + 10, numbers))

print(result)

numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)

"""
Filter : I want to keep only some items.
"""

numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 != 0, numbers))

print(result)

numbers = [1, 2, 3, 4]

result = filter(lambda x: x % 2 == 0, numbers)

print(result)