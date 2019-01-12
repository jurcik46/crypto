class Rsa:

    def __init__(self, pN, pE, pY):
        self.__n = pN
        self.__e = pE
        self.__y = pY

    def getPrime(self, paramNumber):
        num = 1
        while 1:
            num += 2
            if paramNumber % num == 0:
                return num

    def decrypt(self):
        prime = self.getPrime(self.__n)
        q = self.__n / prime
        fi = (prime - 1) * (q - 1)
        d = pow(self.__e, fi - 2, fi)
        print("Fi: ", fi)
        print("d: ", d)
        r = pow(self.__y, d, self.__n)
