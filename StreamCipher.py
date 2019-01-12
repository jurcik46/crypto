import string


class StreamCipher:

    def __init__(self):
        self.__myRand = None

    def my_rand(self):
        self.__myRand = (self.__myRand * 84589 + 45989) % 217728
        return float(self.__myRand) / 217728

    def DecryptText(self, numbere, enText):
        # self.mySeed(key)
        currChar = ''
        self.__myRand = numbere
        # charCount = string.ascii_lowercase
        decryptedText = ""
        try:
            for char in enText:
                pomChar = char.upper()
                if any(v == pomChar for v in string.ascii_lowercase.upper()):
                    indexOfEncryptedChar = ord(pomChar) - ord('A')
                    myRandomNumber = self.my_rand()
                    indexOfStreamCipherChar = int((26 * myRandomNumber))
                    indexOfDecryptedChar = (indexOfEncryptedChar + (26 - indexOfStreamCipherChar)) % 26
                    decryptedText += str((chr((ord('A') + int(indexOfDecryptedChar)))))
                else:
                    decryptedText += str(decryptedText.join(pomChar))
        except ZeroDivisionError:
            print("Unexpected error:", ZeroDivisionError)

        return decryptedText
