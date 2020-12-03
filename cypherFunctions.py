def ceasarCypher(message,key,encrypt) -> str: #Remember to remove message
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    message = message.upper()
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
    return output

def vigenereCypher(message,phrase,encrypt) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    output = ""
    message = message.upper()
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