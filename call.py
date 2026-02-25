import random
Cnumber=random.randrange(3,90)
userInput=int(input("Enter your number:---"))
if userInput<3 or userInput>90:
    print("Invalid number. Please enter a valid number between 3 and 90.")
    print("Your guess number is too high")
elif Cnumber>userInput:
    print("Computer number", Cnumber)
    print("Your guess number is too low")
else:
    print("Computer number", Cnumber)
    print("Your guess number is equal")
