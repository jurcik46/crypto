import string


class VigenerCipherNew:

    def __init__(self):
        self.__en = [0.0856, 0.0139, 0.0279, 0.0378, 0.1304, 0.0289, 0.0199, 0.0526, 0.627, 0.0019, 0.0042, 0.0339,
                     0.0249, 0.0707, 0.0797, 0.0199, 0.0012, 0.0977, 0.0607, 0.1045, 0.0249, 0.0092, 0.0149, 0.0017,
                     0.0199, 0.0008]
        self.__sk = [0.11160, 0.01778, 0.02463, 0.03760, 0.09316, 0.00165, 0.00175, 0.02482, 0.05745, 0.02158, 0.03961,
                     0.04375, 0.03578, 0.05949, 0.09540, 0.03007, 0.00001, 0.04706, 0.06121, 0.05722, 0.03308, 0.04604,
                     0.00001, 0.00028, 0.02674, 0.03064]
        self.__sum = 0.0
        self.__min = 0.0

    def calChiSquareStat(self, cipherBlock):
        freq = []
        freq[:26] = [0] * 26
        strLen = len(cipherBlock)
        ind = 0
        self.__sum = 0
        self.__min = 0
        # a = 0.0
        for i in range(26):
            freq[:26] = [0] * 26
            self.__sum = 0.0
            for ch in range(len(cipherBlock)):
                pom = 0
                if ord(cipherBlock[ch]) - i < 97:
                    pom = ord(cipherBlock[ch]) - i + 26
                else:
                    pom = ord(cipherBlock[ch]) - i
                freq[(pom - ord('a'))] += 1
            for j in range(26):
                chiSquareVal = pow((freq[j] - (strLen * self.__sk[j])), 2) / self.__sk[j] * strLen
                # print(self.__sk[j])
                # chiSquareVal = pow(freq[j] - (strLen * self.__en[j]), 2) / self.__en[j] * strLen
                self.__sum += chiSquareVal
            if i == 0:
                self.__min = self.__sum
                ind = i
            if self.__sum < self.__min:
                self.__min = self.__sum
                ind = i
        return chr(ord('a') + ind)

    def keyLength(self, cipherText):
        p = 1
        zhoda = 0
        arr = []
        arr[:30] = [0] * 30
        for c in range(1, 30):
            for x in range(len(cipherText)):
                if x + c == len(cipherText):
                    break
                if cipherText[x] == cipherText[x + c]:
                    zhoda += 1

            arr[p] = zhoda
            zhoda = 0
            p += 1
        kMax = 0
        max = 0
        for z in range(20, len(arr)):
            if arr[z] > max:
                max = arr[z]
                kMax = z

        print("Key lenght ", kMax)
        return kMax

    def clearTxt(self, txt):
        txt = txt.lower()
        pom = ""
        for i in range(len(txt)):
            if txt[i] in string.ascii_lowercase:
                pom += txt[i]
        return pom

    def decrypt(self, txt, key):
        ret = ""
        txt = txt.lower()
        j = 0
        for i in range(len(txt)):
            c = txt[i]
            if ord(c) < ord('a') or ord(c) > ord('z'):
                ret += c
                continue
            ret += chr((ord(c) - ord(key[j]) + 26) % 26 + ord('a'))
            j += 1
            j = j % len(key)
        return ret.upper()
