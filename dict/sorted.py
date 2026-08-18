marks = {
    "Sajib": 80,
    "Rahim": 95,
    "Karim": 70,
    "Hasan": 90
}

sorted_marks = sorted(
    marks.items(),
    key=lambda item: item[1]
)

print(sorted_marks)


sorted_marks = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True
)

print(sorted_marks)

students = {
    "Sajib": 80,
    "Karim": 70,
    "Rahim": 95
}

result = sorted(students.items())

print(result)


marks = {
    "Sajib": 80,
    "Rahim": 45,
    "Karim": 70,
    "Hasan": 35
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >= 50
}

print(passed)


prices = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

new_prices = {
    fruit: price + 10
    for fruit, price in prices.items()
}

print(new_prices)

student = {
    "name": "Sajib",
    "age": 25,
    "city": "Dhaka"
}

keys = list(student.keys())

print(keys)

items = list(student.items())

print(items)




response = {
    "status": "success",
    "data": {
        "user": {
            "id": 101,
            "name": "Sajib",
            "skills": ["Python", "SQL", "PySpark"]
        }
    }
}

print(response["status"])
print(response["data"]["user"]["name"])
print(response["data"]["user"]["skills"])
print(response["data"]["user"]["skills"][0])