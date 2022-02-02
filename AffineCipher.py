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


def AffineDecryptor(encryptedWord, key_A, key_B):
    decryptedWord = ''

    #finding multiplicative inverse
    a_inverse = 0
    flag = 0

    for x in range(0,26):
        flag = (key_A * x) % 26
        if flag == 1:
            a_inverse = x


    for words in encryptedWord:
        X = mapping[words]

        encodedNumber = (a_inverse*(X - key_B) % 26)

        # Getting key from value
        for key in mapping.keys():
            if encodedNumber == mapping[key]:
                decryptedWord = decryptedWord + key
    return decryptedWord


def AffineEncryptor(encryptedWord, key_A, key_B):
    decryptedWord = ''

    for words in encryptedWord:
        X = mapping[words]

        encodedNumber = (1/key_A)*(X-key_B) % 26
        print(encodedNumber)

        # Getting key from value
        for key in mapping.keys():
            if encodedNumber == mapping[key]:
                decryptedWord = decryptedWord + key
    return decryptedWord

stringToEncrypt = "zbx gcb dbzx rob eleb res xbybegbbe".upper()

splittingString = stringToEncrypt.split()

print("Brute Force Attack Started : ")

for key_A in range (0,26):
    for key_B in range(0,26):
        # print(key_A,key_B)
        for word in splittingString:
            word = AffineDecryptor(word, key_A , key_B)
            print(word, end= " ")
        print(" ")

        