number = input("Enter the number: ")
length = len(number)
sum = 0

for num in number:
    sum += int(num)**length

if sum == int(number):
    print("Number is armstrong")
else:
    print("Not armstrong")