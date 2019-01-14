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

    # n nasobom prvocisel
    def decrypt(self):
        prime = self.getPrime(self.__n)
        print("Prime : ", prime)
        q = self.__n / prime
        print("Q :  ", q)
        fi = (prime - 1) * (q - 1)
        d = self.mul_inv(self.__e, int(fi))
        print("Fi (Verejny): ", int(fi))
        print("d (private) : ", int(d))
        r = pow(self.__y, int(d), self.__n)
        print("Vysledok   ", r)

    def mul_inv(self, a, b):
        b0 = b
        t = 0
        q = 0
        x0 = 0
        x1 = 1
        if b == 1:
            return 1
        while a > 1:
            q = a / b
            t = int(b)
            b = int(a) % b
            a = t
            t = x0
            x0 = x1 - int(q) * x0
            x1 = t
        if x1 < 0:
            x1 += b0
        return x1

    def modInverse(self, a, m):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return 1
