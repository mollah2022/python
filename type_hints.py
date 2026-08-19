def display_Result(num1: int , num2: int) -> int:
    result = num1 + num2
    return result

backResult = display_Result(23,22)

print(backResult)


from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

usr1 = User("Sajib",25,"sajib@gmail.com")

print(usr1)