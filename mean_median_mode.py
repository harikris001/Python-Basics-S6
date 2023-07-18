def median_value(numList):
    # return 0 if list is empty
    if numList == []:
        return 0
    elif len(numList) % 2 == 1:
        # midlle value of list
        return numList[(len(numList)//2)]
    else:
        # average of both middle values
        return (numList[len(numList)//2] + numList[(len(numList)//2) - 1]) / 2
    
def mean_value(numList):
    # return 0 if list is empty
    if numList == []:
        return 0
    sum = 0
    for num in numList:
        sum += num
    # Return average value
    return sum/len(numList)

def mode_value(numList):
    # return 0 if list is empty
    if numList == []:
        return 0
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

numbers  = []

def main(numbers):
    print(f"median value: {median_value(numbers)}")
    print(f"Mean value: {mean_value(numbers)}")
    print(f"Mode value: {mode_value(numbers)}")

main(numbers)