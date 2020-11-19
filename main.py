#Setup
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptAccept = ["ENCRYPT","E"]
decryptAccept = ["DECRYPT","D"]
accepted = encryptAccept + decryptAccept
mode = "default"

#Functions
def keyEncryption(message: str,key,encrypt) -> str:
    output = ""
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol) ## Retrieves number associated with the letters
            if encrypt == True:
                num = num + key
            else:
                num = num - key
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

def bruteForce(message: str) -> str:
    for key in range(len(letters)):
        output = ""
        for symbol in message:
            if symbol in letters:
                num = letters.find(symbol) ## Retrieves number associated with the letters
                num = num - key
            ## Wrap-around protection
            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)
            ## Adding generated letter to translated array
            output = output + letters[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
        print("Key: {0}. Message: {1}".format(key,output))

#Main
while mode not in accepted:
    mode = input("Would you like to encrypt[e] a message, or decrypt[d] a message?\n")
    mode = str(mode.upper())
    if mode == "EXIT":
        exit()
print("Mode set to {0}".format(mode))

if mode in encryptAccept:
    key = int(input("Please enter the key to be used:\n"))
    text = input("Please enter the text to be encrypted:\n")
    text = text.upper()
    message = keyEncryption(text,key,encrypt=True)
    print(message)
elif mode in decryptAccept:
    keyKnown = input("Is the encryption key known? Yes/No:\n")
    keyKnown = keyKnown.upper()
    if keyKnown in {"YES","Y"}:
        key = int(input("Please enter the key to be used:\n"))
        text = input("Please enter the text to be decoded:\n")
        text = text.upper()
        message = keyEncryption(text,key,encrypt=False)
        print(message)
    else:
        text = input("Please enter the text to be decoded:\n")
        text = text.upper()    
        bruteForce(text)
else:
    print("Sorry, something went wrong.")
    exit()
