def AtbashEncrpytor(inputString):
    cipherText = ''
    for character in inputString:
    
        asci = ord(character)
        
        if asci >= 65 and asci <= 90:
            position = asci - 65
            position = 25 - position
            asci = position + 65
            character = chr(asci)
            cipherText = cipherText + character
    
    return cipherText

inputString = input("Enter Your Text To  Encrpt/Decrypt : ")
print(AtbashEncrpytor(inputString.upper()))