def find_number(numbers, target):

    for number in numbers:
        if number == target:
            return number

    return None

result = find_number([10, 20, 30], 20)

if result is not None:
    print("Found:", result)
else:
    print("Not found")