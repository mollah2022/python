number  = 10

for i in range(1, 6):
     if i == 3:
         break
     print(f"i is a {i}")

print("+++++++++------------------++++++++++")

for i in range(1, 6):
    if i == 3:
        continue
    print(f"i is a {i}")

for i in range(10):
    print(f"I is a {i} ")

print("+++++++++------------------++++++++++")

for i in range(2,10):
    print(f"I is a {i} ")

print("+++++++++------------------++++++++++")

for i in range(2,10,2):
    print(f"I is a {i} ")

print("+++++++++------------------++++++++++")

for i in range(10,0,-1):
    print(f"I is a {i} ")

print("+++++++++------------------++++++++++")

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print("+++++++++------------------++++++++++")

while number <=10:
    print(f"Number is {number}")
    number += 1 

print("+++++++++------------------++++++++++")

while number >=0:
    print(f"Number is {number}")
    number -= 1
