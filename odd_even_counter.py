n = int(input("Enter the number of items: "))
odd,even = 0,0
print("Enter the Numbers: ")
for i in range(n):
    num = int(input())

    if num%2 == 0:
        odd +=1
    else:
        even +=1

print(f"Odd Numbers: {odd}, Even Numbers: {even}")
