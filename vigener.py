from FreqAnalys import FreqAnalys
from StreamCipher import StreamCipher
from joblib import Parallel, delayed
import multiprocessing

# fre = FreqAnalys("sk")
# encryptedText = "asdasdasdasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdfg"
# print(len(fre.freq))
# print(fre.freq['a'])

# print(fre.Difference("asdasdasdasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdfg"))

variance = 0.02
fileName = "prudovaSifraTexts/text1_enc.txt"
file_object = open(fileName, "r")
# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(1000000)
encryptedText = file_object.read()


# num_cores = multiprocessing.cpu_count()


def processInput(i):
    streamCIpher = StreamCipher(i)
    decryptedText = streamCIpher.DecryptText(encryptedText)

    freAnalysis = FreqAnalys("sk")
    try:
        # print(i)
        if freAnalysis.Difference(decryptedText) <= variance:
            print("Key " + i + " -> " + decryptedText[:60])
    except ZeroDivisionError:
        print("Unexpected error:", ZeroDivisionError)


# multiprocessing.cpu_count()
results = Parallel(n_jobs=1)(delayed(processInput)(i) for i in inputs)
print("END")
input = input("Enter key :")

f = StreamCipher(int(input))
text = f.DecryptText(encryptedText)
text.join("   Key: ", input)

print(text)
# fileName.join(".decoded.txt")
file = open(fileName.join(".decoded.txt"), "w")
file.write(text)

file_object.close()
file.close()
