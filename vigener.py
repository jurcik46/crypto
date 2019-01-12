from FreqAnalys import FreqAnalys
from StreamCipher import StreamCipher
from joblib import Parallel, delayed
import multiprocessing

# encryptedText = "asdasdasdasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdfg"
# print(len(fre.freq))
# print(fre.freq['a'])
# fre = FreqAnalys("sk")
# print(fre.Difference("asdasdasdasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdfg"))
# print(fre.Difference(
#     "asdasdasdasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdfasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdfasxcvmxcvvjbkjnkjjktherkjntketjkfsdjkgnjkfdgdffg"))
# print(fre.Difference(
#     "yxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxc"))

streamCIpher = StreamCipher(100)
streamCIpher.DecryptText(
    "yxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxcyxc");
exit(0)
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
results = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(processInput)(i) for i in inputs)
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
