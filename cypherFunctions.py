def ceasarCypher(encrypt) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    message = str(input("Please enter the text to be encrypted: \n"))
    message = message.upper()
    key = int(input("Please enter an integer to use as the encryption key: \n"))
    for symbol in message:
        if symbol in alphabet:
            num = alphabet.find(symbol) ## Retrieves number associated with the alphabet
            if encrypt == True:
                num = num + key
            else:
                num = num - key
            ## Wrap-around protection
            if num >= len(alphabet):
                num = num - len(alphabet)
            elif num < 0:
                num = num + len(alphabet)
            ## Adding generated letter to translated array
            output = output + alphabet[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
    print("Task complete. Translated task below: \n")
    print(output)

def vigenereCypher(encrypt) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    output = ""
    message = str(input("Please enter the text to be encrypted: \n"))
    message = message.upper()
    phrase = str(input("Please enter a phrase to use as the encryption key: \n"))
    phrase =  phrase.upper()
    for symbol in message:
        if i == len(phrase):
            i = i - len(phrase)
        if symbol in alphabet:
            num = alphabet.find(symbol)
            shiftFactor = alphabet.find(phrase[i])
            if encrypt == True:
                num = num + shiftFactor
            else:
                num = num - shiftFactor
            ## Wrap-around protection
            if num >= len(alphabet):
                num = num - len(alphabet)
            elif num < 0:
                num = num + len(alphabet)
            i = i + 1
            ## Adding generated letter to translated array
            output = output + alphabet[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
    return output

def bruteForce(message: str) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(alphabet)):
        output = ""
        for symbol in message:
            if symbol in alphabet:
                num = alphabet.find(symbol) ## Retrieves number associated with the alphabet
                num = num - key
            ## Wrap-around protection
            if num >= len(alphabet):
                num = num - len(alphabet)
            elif num < 0:
                num = num + len(alphabet)
            ## Adding generated letter to translated array
            output = output + alphabet[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
        print("Key: {0}. Message: {1}".format(key,output))