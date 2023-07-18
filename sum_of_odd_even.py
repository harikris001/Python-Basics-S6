upper = int(input("Enter upper limit: "))
lower = int(input("Enter lower limit: "))
odd_sum,even_sum  = 0,0


for i in range(lower, upper):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Odd sum {odd_sum}")
print(f"Even sum {even_sum}")