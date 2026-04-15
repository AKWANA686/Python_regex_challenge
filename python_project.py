# Write a Python program that checks whether a number entered by the user is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0 and number % 2 != 0:
    print("The number is even.")
else:
    print("The number is odd.")