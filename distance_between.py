import math

print("Point 1")
x1 = float(input("X1 cordinate: "))
y1 = float(input("Y1 cordinate: "))

print("Point 2")
x2 = float(input("X2 cordinate: "))
y2 = float(input("Y2 cordinate: "))

distance = math.sqrt(((x2-x1)**2 + (y2-y1)**2))

print(f"Distance between = {distance}")