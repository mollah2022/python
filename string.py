name = "SajibAhmed"

print(name)

print(f"first index is {name[0]}")

print(f"last index is {name[-1]}")

print(f"length of the string is {len(name)}")

print(f"substring(slice) from index 0 to 5 is {name[0:6]}")

print(f"substring(slice) from index 2 to 7 is {name[2:8]}")

print(f"substring(slice) from index 0 to 5 with step 2 is {name[0:6:2]}")

print(f"Converting string to uppercase: {name.upper()}")

print(f"Converting string to lowercase: {name.lower()}")

print(f"Replacing 'Sajib' with 'John': {name.replace('Sajib', 'John')}")

print(f"Finding index of 'A': {name.find('A')}")

print(f"Checking if string starts with 'Sajib': {name.startswith('Sajib')}")

print(f"Checking if string ends with 'Ahmed': {name.endswith('Ahmed')}")

name_with_whitespace = "   SajibAhmed   "

print(f" Use Strip to remove whitespace from the beginning and end of the string: {name_with_whitespace.strip()}")

string = "I am learning Python programming."

print(f"Splitting the string into a list of words: {string.split()}")
