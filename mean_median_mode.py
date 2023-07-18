def median_value(numList):
    if len(numList) % 2 == 1:
        # midlle value of list
        return numList[(len(numList)//2)]
    else:
        # average of both middle values
        return (numList[len(numList)//2] + numList[(len(numList)//2) - 1]) / 2
    
def mean_value(numList):
    sum = 0
    for num in numList:
        sum += num
    # Return average value
    return sum/len(numList)

def mode_value(numList):
    # filtering unique elements from list
    unique_numList = list(set(numList))
    max_freq = 0
    for num in unique_numList:
        # getting frequency of element from list
        freq = numList.count(num)
        if max_freq < freq:
            max_freq = freq
            mode = num
    return mode

numbers  = input("Enter numbers with spaces: ")

numbers = list(map(int,numbers.strip().split(' '))) # strip is used to remove blank space in front and back of input string
                                                    # split will split the string at the spaces.

print(f"median value: {median_value(numbers)}")
print(f"Mean value: {mean_value(numbers)}")
print(f"Mode value: {mode_value(numbers)}")
