def display(name,age,gender):
    print(f"My name is {name} i am {age} year old and i am {gender}")


display(name="sajib",age=22,gender="Male")


def displayInfo(name,age,gender):
    print(f"My name is {name} i am {age} year old and i am {gender}")

displayInfo("sajib", age=23,gender="male")

def displayInfo(name,age,gender):
    print(f"My name is {name} i am {age} year old and i am {gender}")

displayInfo("Mofiz",age=32,gender="male")



def cal(*args):
    sum = 0

    for arg in args:
        sum += arg

    return sum


print(cal(1,2,3,4))
print(cal(2,3,4,5,6,7,8))
print(cal(10,11,22,55,11,10,32))


def DisplayInfo(**kwargs):

    print(kwargs)


DisplayInfo(name="Atik",age=22,salary=25500,gender="Male",hobby=["gaming","movie","drama"])

