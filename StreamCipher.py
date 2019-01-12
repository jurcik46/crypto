import string
import sys
import time


class StreamCipher:

    def __init__(self, sed):
        self.__myRand = sed

    def my_rand(self):
        self.__myRand = (84589 * self.__myRand + 45989) % 217728
        return self.__myRand / 217728.0

    # def mySeed(self, sed):
    #     self.__myRand = sed

    def DecryptText(self, numbere, enText):
        # self.mySeed(key)
        currChar = ''
        self.__myRand = numbere
        # charCount = string.ascii_lowercase
        decryptedText = ""
        try:
            for char in enText:
                pomChar = char.lower()
                if any(v == pomChar for v in string.ascii_lowercase):
                    indexOfEncryptedChar = ord(pomChar) - ord('a')
                    myRandomNumber = self.my_rand()
                    # print(self.__myRand)
                    # time.sleep(0.3)
                    indexOfStreamCipherChar = (26 * myRandomNumber)
                    # print(indexOfStreamCipherChar)
                    # print(myRandomNumber)

                    indexOfDecryptedChar = (indexOfEncryptedChar + (26 - indexOfStreamCipherChar)) % 26
                    decryptedText += str((chr((ord('a') + int(indexOfDecryptedChar)))))
                else:
                    decryptedText += str(decryptedText.join(pomChar))
        except ZeroDivisionError:
            print("Unexpected error:", ZeroDivisionError)

        return decryptedText
