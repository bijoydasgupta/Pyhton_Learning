print("\nFor Loops:")
for number in range(3):
    print("attempt")
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")
for number in range(1, 5):
    print("attempt", number, number * ".")
for number in range(1, 10, 3):
    print("attempt", number, number * ".")


print("\n\nFor...else:")
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times & failed")
