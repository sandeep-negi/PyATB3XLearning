print("Factorial of a number Program")

num = int(input("Enter a number : "))

fact = 1
while num != 0:
    fact = fact * num
    num -= 1

print("Factorial of a number {} is {}".format(num, fact))
