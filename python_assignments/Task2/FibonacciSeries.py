print("Fibonacci Series")
# 0 1 1 2 3 5 8 13 21 34
n = int(input("Find fibonacci up-to number : "))
a, b = 0, 1
print(a, b, end=" ")
for i in range(2, n):
    b = b + a
    a = b - a
    print(b, end=" ")
