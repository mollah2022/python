numbers = [2,4,5,6,7,8]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class Count:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


numbers = Count(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))



numbers = [10, 20, 30]

for number in numbers:
    print(number)


it = iter(numbers)

while True:
    try:
        number = next(it)
        print(number)
    except StopIteration:
        break



