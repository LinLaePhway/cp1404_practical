"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Questions
When will a ValueError occur?
A ValueError will occur if a non-integer value is entered for either the numerator or the denominator.

When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if 0 is entered as the value for the denominator.

Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can change the code to avoid the possibility of a ZeroDivisionError by adding a condition to check if the 
denominator is zero before performing the division operation.
"""