"""
1) Develop a Python script that calculates the square and cube of a given number.
num = 2, sq = 4, cu=8
"""

# Program
print(" Square and Cube of a number ")
num = int(input("Enter a number : "))
sq = num ** 2
cu = num ** 3

print("square of number {} is {}".format(num, sq))
print("cube of a number {} is {}".format(num, cu))
"""

2) WAP that takes two number as input and prints whether the number is greater than,
less than or are equal to each other.
"""
print(" Comparison of two numbers ")
# Program
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

if num1 > num2:
    print("number1 is greater than number2")
elif num1 < num2:
    print("number1 is less than number2")
else:
    print("number1 is equal to number2")

