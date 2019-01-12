import string
import time


class FreqAnalys:

    def __init__(self, lang):
        self.__freq = dict()
        if lang == "sk":
            self.skCharacter()
        else:
            self.enCharacter()

    def Difference(self, text):
        charSum = 1
        charCount = dict.fromkeys(string.ascii_lowercase.upper(), 0)

        for char in text:
            if char.upper() in charCount.keys():
                charSum += 1
                charCount[char.upper()] += 1

        diff = 0
        for key, value in charCount.items():
            pom = value / charSum - self.freq[key]
            diff += abs(pom)
        return diff / len(self.freq)

    def skCharacter(self):
        self.__freq = {
            "A": 0.1116,
            "B": 0.0178,
            "C": 0.0246,
            "D": 0.0376,
            "E": 0.0931,
            "F": 0.0017,
            "G": 0.0018,
            "H": 0.0248,
            "I": 0.0575,
            "J": 0.0216,
            "K": 0.0396,
            "L": 0.0438,
            "M": 0.0358,
            "N": 0.0595,
            "O": 0.0954,
            "P": 0.0301,
            "Q": 0.0000,
            "R": 0.0471,
            "S": 0.0612,
            "T": 0.0572,
            "U": 0.0331,
            "V": 0.0460,
            "W": 0.0000,
            "X": 0.0003,
            "Y": 0.0267,
            "Z": 0.0306,
        }

    def enCharacter(self):
        self.__freq = {
            "A": 0.0804,
            "B": 0.0154,
            "C": 0.0306,
            "D": 0.0399,
            "E": 0.1251,
            "F": 0.0230,
            "G": 0.0196,
            "H": 0.0549,
            "I": 0.0726,
            "J": 0.0016,
            "K": 0.0067,
            "L": 0.0414,
            "M": 0.0253,
            "N": 0.0709,
            "O": 0.0760,
            "P": 0.0200,
            "Q": 0.0011,
            "R": 0.0612,
            "S": 0.0654,
            "T": 0.0925,
            "U": 0.0271,
            "V": 0.0099,
            "W": 0.0192,
            "X": 0.0019,
            "Y": 0.0173,
            "Z": 0.0009,
        }

    @property
    def freq(self):
        return self.__freq
