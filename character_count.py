text = input("Enter the text: ")
freq = []

for i in range(len(text)):
    freq.append(0)

char_dict = dict()

for char in text:
    if char_dict.get(char,None) == None:
        char_dict[char] = 1
    else:
        char_dict[char] += 1

print(char_dict)