f = open("in.txt","r")
text = f.read()
words = list(text.split(' '))
count = 0

for word in words:
    if len(word) == 4:
        count += 1
print(f"Four letter word Count: {count}")

f.close()