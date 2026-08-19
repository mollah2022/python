file = open("index.html","r")
read = file.read()
print(read)


file1 = open("index.html",'a')
append = file1.write("\nThis is my second line in python code")


file = open("index.html","r")
read = file.read()
print(read)

file.close()


file = open("new_file.txt","x")
file.write("Hello World. i am new programmer in town")

file1 = open("new_file.txt","r")
read = file1.read()
print(read)

file1.close()