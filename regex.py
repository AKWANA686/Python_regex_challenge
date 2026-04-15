# Write a Python program that uses regular expressions (`re` module) to extract all numbers from a string.
import re

word = input("Enter a string: ")
numbers = re.findall(r"\d+", word)
if numbers:
    print("Numbers found in here:", numbers)
else:
    print("No matches found.")