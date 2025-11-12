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

print("\nTernary Operator:")
Age = 22
text = "Eligible" if Age >= 18 else "Not eligible"
print(text)
