text = input("Enter the text: ")

# open and write file
f = open("out.txt","w")
f.write(text)
f.close()

# read file
f = open("out.txt","r")
print("Entered text: " + f.read())
f.close()