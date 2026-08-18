student = {
    "name": "Sajib",
    "age": 25,
    "city": "Dhaka"
}


for key in student:
    print(key)

for value in student.values():
    print(value)


user = {
    "name": "Sajib",
    "profile": {
        "age": 25,
        "address": {
            "city": "Dhaka",
            "country": "Bangladesh"
        }
    }
}

print(user["profile"]["address"]["country"])


data = {
    "name": "Sajib",
    "orders": [
        {
            "id": 101,
            "product": "Laptop"
        },
        {
            "id": 102,
            "product": "Mouse"
        }
    ]
}


print(data["orders"])