#Setup
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
accepted = ["ENCRYPT","DECRYPT","E","D"]
mode = "default"

#Functions
def encryption(message: str,key) -> str:
    output = ""
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol) ## Retrieves number associated with the letters
            num = num + key
            ## Wrap-around protection
            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)
            ## Adding generated letter to translated array
            output = output + letters[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
    return output

def decryption(input: str,key) -> str:

    return "blank"

#Main
while mode not in accepted:
    mode = input("Would you like to encrypt[E] a message, or decrypt[D] a message?\n")
    mode = mode.upper()
    if mode == "EXIT":
        exit()
print("Mode set to {0}".format(mode))

key = int(input("Please enter the key to be used:\n"))
text = input("Please enter the text to be used:\n")
text = text.upper()

if mode == accepted[0] or accepted[2]:
    message = encryption(text,key)
elif mode == accepted[1] or accepted[3]:
    message = decryption(text,key)

print(message)