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
        charCount = dict.fromkeys(string.ascii_lowercase, 0)

        for char in text:
            if char.lower() in charCount.keys():
                charSum += 1
                # print(char)
                # print(charCount[char.lower()])
                charCount[char.lower()] += 1
                # print(charCount[char.lower()])

        diff = 0
        for key, value in charCount.items():
            pom = value / charSum - self.freq[key]
            diff += abs(pom)
        # a = diff / len(self.freq)
        # print(diff / len(self.freq))
        return diff / len(self.freq)

    def skCharacter(self):
        self.__freq = {
            "a": 0.1116,
            "b": 0.0178,
            "c": 0.0246,
            "d": 0.0376,
            "e": 0.0931,
            "f": 0.0017,
            "g": 0.0018,
            "h": 0.0248,
            "i": 0.0575,
            "j": 0.0216,
            "k": 0.0396,
            "l": 0.0438,
            "m": 0.0358,
            "n": 0.0595,
            "o": 0.0954,
            "p": 0.0301,
            "q": 0.0000,
            "r": 0.0471,
            "s": 0.0612,
            "t": 0.0572,
            "u": 0.0331,
            "v": 0.0460,
            "w": 0.0000,
            "x": 0.0003,
            "y": 0.0267,
            "z": 0.0306,
        }

    def enCharacter(self):
        self.__freq = {
            "a": 0.0804,
            "b": 0.0154,
            "c": 0.0306,
            "d": 0.0399,
            "e": 0.1251,
            "f": 0.0230,
            "g": 0.0196,
            "h": 0.0549,
            "i": 0.0726,
            "j": 0.0016,
            "k": 0.0067,
            "l": 0.0414,
            "m": 0.0253,
            "n": 0.0709,
            "o": 0.0760,
            "p": 0.0200,
            "q": 0.0011,
            "r": 0.0612,
            "s": 0.0654,
            "t": 0.0925,
            "u": 0.0271,
            "v": 0.0099,
            "w": 0.0192,
            "x": 0.0019,
            "y": 0.0173,
            "z": 0.0009,
        }

    @property
    def freq(self):
        return self.__freq
