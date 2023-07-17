numbers = input("Enter numbers with a space: ")

# remove space in front and back using strip
# then split the text with space using split function
num_list = list(map(int,numbers.strip().split(" ")))

def min_max(numberList):

    small,large = numberList[0],numberList[0]

    for i in range(len(numberList)):
        if small > numberList[i]:
            small = numberList[i]
        if large < numberList[i]:
            large = numberList[i]
    
    return small,large

min,max = min_max(numberList=num_list)

print(min,max)