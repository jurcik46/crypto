import string
import sys


class StreamCipher:

    def __init__(self, sed):
        self.__myRand = sed

    def my_rand(self):
        self.myRand = (84589 * self.__myRand + 45989) % 217728
        return self.__myRand / 217728.0

    # def mySeed(self, sed):
    #     self.__myRand = sed

    def DecryptText(self, enText):
        # self.mySeed(key)
        currChar = ''
        # charCount = string.ascii_lowercase
        decryptedText = ""
        try:
            for char in enText:
                pomChar = char.lower()
                if any(v == pomChar for v in string.ascii_lowercase):
                    indexOfEncryptedChar = ord(pomChar) - ord('a')
                    myRandomNumber = self.my_rand()
                    indexOfStreamCipherChar = (26 * myRandomNumber)

                    indexOfDecryptedChar = (indexOfEncryptedChar + (26 - indexOfStreamCipherChar)) % 26
                    decryptedText = decryptedText.join(('A' + chr(int(indexOfDecryptedChar))))
                else:
                    decryptedText = decryptedText.join(pomChar)
        except ZeroDivisionError:
            print("Unexpected error:", ZeroDivisionError)

        print("text decrypted:", decryptedText)
        return decryptedText
