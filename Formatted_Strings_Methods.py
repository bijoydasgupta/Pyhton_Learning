print()  # New Line
a = "Hello"
b = "World"
c = a + " " + b
print(c)

print()  # New Line
first = "Bijoy"
last = "Das"
full = f"{first}{last}"
fullName = f"{first} {last}"
print(full)
print(fullName)

print()  # New Line
result = f"{len(first)} {2+2}"
print(result)

print()  # New Line
greet = " hellO worLd"
print(greet.upper())  # HELLO WORLD
print(greet.lower())  # hello world
print(greet.title())  # Hello World
print(greet.strip())  # spaces will  be gone

print(greet.find("Pro"))  # -1
print(greet.replace('O', ' '))  # hell  worLd

print()  # New Line
print("hell" in greet)  # True
print("pro" not in greet)  # True
