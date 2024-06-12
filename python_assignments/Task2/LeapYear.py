"""
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
"""

print("Leap Year Program")

leapYear = int(input("Enter year : "))

if (leapYear % 4 == 0 and leapYear % 100 != 0) or (leapYear % 400 == 0) :
    print("It is a leap Year")
else:
    print("It is not a leap Year")
