user1 = {
    "name": "Sajib",
    "age": 25
}

user2 = {
    "city": "Dhaka",
    "country": "Bangladesh"
}


user1.update(user2)

print(user1)


new_user = {
    **user1
}

print(user1)



user1 = {
    "name": "Sajib",
    "age": 25
}

user2 = {
    "city": "Dhaka",
    "country": "Bangladesh"
}

user1 = {
    "name": "Sajib",
    "age": 25
}

user2 = {
    "city": "Dhaka",
    "country": "Bangladesh"
}

user3 = {
    **user1,
    **user2
}

user3 = {
    **user1,
    **user2
}

print(user3)
