import math  # It will works from 27 no. line
print()  # New Line
x = 1
y = 1.123
z = 1 + 2j
print(x)
print(y)
print(z)

print()  # New Line
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)  # 10 ^ 3

print()  # New Line
a = 10
a = a + 3  # that can be written as a += 3
print(a)

print()  # New Line
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))  # From Math Library

print()  # New Line
x = input("x: ")
# print(type(x))
""" 
Type Conversion:
int(x)
float(x)
bool(x)
str(x)
"""
y = int(x)+1
print(f"x: {x}, y: {y}")

print("\nIn Boolean Context:")  # New Line
print(bool(0))  # False
print(bool(4))  # True
print(bool(-5))  # True
print(bool(""))  # False
print(bool("FALSE"))  # True
print(bool())  # False
