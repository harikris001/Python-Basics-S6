text = input("Enter the message: ")
distance = int(input("Enter the key: "))
option = int(input("To decrypt->1, To encrypt->0: "))


def caesar_encrypt(text):
    encrypt = ''
    for char in text:
        value = ord(char)
        value += distance
        if value > ord('z'):
            value = ord('a') + distance - (ord('z') - value + 1)
        encrypt += chr(value)
    return encrypt

def caesar_decrypt(text):
    decrypt = ''
    for char in text:
        value = ord(char)
        value -= distance
        if value < ord('a'):
            value = ord('z') - distance + (value - ord('a') + 1)
        decrypt += chr(value)
    return decrypt

if option==1:
    print(caesar_decrypt(text))
else:
    print(caesar_encrypt(text))