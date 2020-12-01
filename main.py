import cypherFunctions

def modeSelect():
    accepted = [1, 2]
    mode = "default"
    while mode not in accepted:
        mode = int(input("Please select a mode: \n [1] Encrypt \n [2] Decrypt \n [0] Exit \n"))
        if mode == 0:
            exit()
        if mode not in accepted:
            print("Input not recognised. Please type either '1' for encrypt, or '2' for decrypt. \nType '0' to exit the application.")
    return mode

def launchEncryption():
    accepted = [1,2]
    mode = "default"
    while mode not in accepted:
        mode = int(input("Please select an encryption type for your message: \n[1] Ceasar Cypher \n[2] Vigenere Cypher \n[0] Exit \n"))
        if mode == 0:
            exit()
        if mode == 1:
            cypherFunctions.ceasarCypher(encrypt=True)
        if mode == 2:
            cypherFunctions.vigenereCypher(encrypt=True)

def launchDecryption():
    accepted = [1,2,3]
    mode = "default"
    while mode not in accepted:
        mode = int(input("Please select a decryption type for your message: \n[1] Ceasar Cypher \n[2] Vigenere Cypher \n[3] Unknown (Brute Force) \n[0] Exit \n"))
        if mode == 0:
            exit()
        if mode == 1:
            cypherFunctions.ceasarCypher(encrypt=False)
        if mode == 2:
            cypherFunctions.vigenereCypher(encrypt=False) 
        if mode == 3:
            print("Mode not yet implemented")

mode = modeSelect()
if mode == 1:
    launchEncryption()
else:
    launchDecryption()