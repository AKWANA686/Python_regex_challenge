# Write a Python program that checks whether a number entered by the user is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Write a program that calculates the sum of numbers from 1 up to a given number.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print(f"The sum from 1 to {n} is: {sum}")