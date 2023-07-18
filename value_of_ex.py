import math

x = int(input("Enter the value of X: "))
n = int(input("Enter the value of n: "))
sum = 0

for i in range(n):
    sum += x**i/math.factorial(i)

print(sum)