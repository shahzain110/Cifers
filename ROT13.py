def Rot13(inputString):
    cipherText = ''
    for character in inputString:
    
        asci = ord(character)
        
        if asci >= 65 and asci <= 90:
            position = asci + 13
            if position > 90:
                difference = position - 90
                position = 64
                position += difference

        character = chr(position)
        cipherText = cipherText + character
    
    return cipherText

inputString = input("Enter Your Text To  Encrpt/Decrypt : ")
print("Your Encrpted Text is ")
print(Rot13(inputString.upper()))