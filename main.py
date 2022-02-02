mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

inputString = ''


def Encryptor(inputString):
    encryptedWord = ''
    for words in inputString:
        X = mapping[words]
        # key is 19
        encodedNumber = (1972 + X) % 26
        # Getting key from value
        for key in mapping.keys():
            if encodedNumber == mapping[key]:
                encryptedWord = encryptedWord + key
    return encryptedWord


def Decryptor(encryptedWord):
    decryptedWord = ''
    for words in encryptedWord:
        X = mapping[words]
        # key is 19
        encodedNumber = (X - 24) % 26
        # Getting key from value
        for key in mapping.keys():
            if encodedNumber == mapping[key]:
                decryptedWord = decryptedWord + key
    return decryptedWord


stringToDecrypt = "Amlepyrsjyrgmlq wmsp npmepyk qsaacqqdsjjw qmjtcq rfc qfgdr agnfcp".upper()
stringToEncrypt = "Welcome back to university its being long ago to teach in the classroom".upper()

splittingString = stringToEncrypt.split()
print("The Decrypted Words are : ")
for word in splittingString:
    print(Encryptor(word), end=' ')

print(" ")
splittingString = stringToDecrypt.split()
print("The Encrypted Words are : ")
for word in splittingString:
    print(Decryptor(word), end=' ')
