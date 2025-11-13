# Comparison Operators
print("\nComparison Operators:")
print("10 > 3:", 10 > 3)
print("10 >= 3:", 10 >= 3)
print("10 < 20:", 10 < 20)
print("10 <= 3:", 10 <= 20)
print("10 == 10:", 10 == 10)
print("10 == '10':", 10 == "10")
print("10 != '10':", 10 != "10")
print("'bg' < 'dog':", 'bg' < 'dog')
print("'bg' == 'BG':", 'bg' == 'BG')


# Conditional Statements
print("\nConditional Statements:")
temperture = 15
if temperture > 30:
    print("It's hot")
    print("Drink water")
elif temperture > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# Ternary Operator
print("\nTernary Operator:")
Age = 22
text = "Eligible" if Age >= 18 else "Not eligible"
print(text)


# Logical Operators
print("\nLogical Operators:")
high_income = True
good_credit = False
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

student = True
if not student:
    print("The person is eligible")
else:
    print("The person is not eligible")

high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("He is Eligible")
else:
    print("He is not Eligible")


# Short-circuit Evaluations
print("\nShort-circuit Evaluations:")
high_income = True
good_credit = True
student = True
if high_income and good_credit and not student:
    print("The student is eligible")
else:
    print("The student is not eligible")
if high_income or good_credit or not student:
    print("The person is eligible")
else:
    print("The person is not eligible")

# Chaining Comparison Operators
print("\nChaining Comparison Operators:")
age = 22
if 18 <= age < 65:
    print("Eligible Employee")
else:
    print("Not Eligible Employee")
