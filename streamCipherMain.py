from joblib import Parallel, delayed
from StreamCipher import StreamCipher
from FreqAnalys import FreqAnalys
import multiprocessing


def processInput(i, encryptedText, variance):
    decryptedText = stream.DecryptText(i, encryptedText)
    try:
        if fre.Difference(decryptedText) <= variance:
            print("Kluč " + str(i) + "  Text:  " + decryptedText[:150])
        # print("Key " + str(i))
    except ZeroDivisionError:
        print("Unexpected error:", ZeroDivisionError)


# 0.0667 EN
# 0.06027 SK

fre = FreqAnalys("sks")
stream = StreamCipher()
variance = 0.02
fileName = "prudovaSifraTexts/text4_enc.txt"
file_object = open(fileName, "r")
inputs = range(55000, 100000)
encryptedText = file_object.read()
Parallel(n_jobs=multiprocessing.cpu_count())(
    delayed(processInput)(i, encryptedText, variance) for i in inputs)
# for x in inputs:
#     processInput(x, encryptedText, variance)
print("END")
key = input("Enter key :")

text = stream.DecryptText(int(key), encryptedText)
text += str(("   Key: ", str(key)))

print(text)
file = open(fileName + str(".decoded.txt"), "w")
file.write(text)

file_object.close()
file.close()
