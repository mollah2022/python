try:
    number = int(input("Please enter a Number "))
    print(number)
except:
    print("Please enter a valid number")



try:
    number = int(input("Enter number: "))
    result = 10 / number

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("You cannot divide by zero")


try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number")

else:
    print("You entered:", number)

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")


try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Done")


class AgeError(Exception):
    pass


try:
    age = -10

    if age < 0:
        raise AgeError("Age cannot be negative")

except AgeError as e:
    print(e)


def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount

def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount