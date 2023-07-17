n = int(input("Enter the max range of numbers: "))
flag = 0

for i in range(2,n):
    num = i
    a = 2
    while a <= num//2:
        if num % a == 0:
            flag = 1
            break
        a += 1
    if flag == 0:
        print(i)
    flag = 0