#Setup
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptAccept = ["ENCRYPT","E"] #Assigning accepted phrases. Can be easily updated if, for example, users consistently typo encrpyt
decryptAccept = ["DECRYPT","D"]
accepted = encryptAccept + decryptAccept
mode = "default" #Setting this to default allows the while loop statement below to work, kickstarting the application
advanced = True

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

def advancedEncryption(message: str,phrase: str,encrypt) -> str:
    i = 0
    output = ""
    for symbol in message:
        if i == len(phrase):
            i = i - len(phrase)
        if symbol in letters:
            num = letters.find(symbol)
            shiftFactor = letters.find(phrase[i])
            if encrypt == True:
                num = num + shiftFactor
            else:
                num = num - shiftFactor
            ## Wrap-around protection
            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)
            i = i + 1
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

if mode in encryptAccept and advanced == False:
    key = int(input("Please enter the key to be used:\n"))
    text = input("Please enter the text to be encrypted:\n")
    text = text.upper()
    message = keyEncryption(text,key,encrypt=True)
    print(message)
elif mode in decryptAccept and advanced == False:
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
elif mode in encryptAccept and advanced == True:
    print("Advanced Mode\n")
    phrase = input("Please enter the encryption phrase:\n")
    phrase = phrase.upper()
    text = input("Please enter the text to be encrypted:\n")
    text = text.upper()
    message = advancedEncryption(text,phrase,encrypt=True)
    print(message)
elif mode in decryptAccept and advanced == True:
    print("Advanced Mode\n")
    phrase = input("Please enter the encryption phrase:\n")
    phrase = phrase.upper()
    text = input("Please enter the text to be decrypted:\n")
    text = text.upper()
    message = advancedEncryption(text,phrase,encrypt=False)
    print(message)
else:
    print("Sorry, something went wrong.")
    exit()
