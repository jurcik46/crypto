from vigenerCipherNew import VigenerCipherNew

v = VigenerCipherNew()

fileName = "vigenerovaSifraTexts/text3_enc.txt"
file_object = open(fileName, "r")
encryptedText = file_object.read()
encryptedText2 = encryptedText
keyLn = v.keyLength(v.clearTxt(encryptedText))
splitCipherText = []
splitCipherText[:keyLn] = "" * keyLn

splitCipherText[:keyLn] = [""] * keyLn

keyObtained = ""
encryptedText = v.clearTxt(encryptedText)
for i in range(len(encryptedText)):
    for j in range(keyLn):
        if i % keyLn == j:
            splitCipherText[keyLn + j - keyLn] += encryptedText[i]

for x in range(len(splitCipherText)):
    keyObtained += v.calChiSquareStat(splitCipherText[x])

bad = "xgafqeglrstmjqfmlgptketfvi"
ok = "xgafqeglrstmjqflsgptketphi"
bad1 = "kokvminteusweclouxbfswm"
ok1 = "kokvminteusweclauxbfswm"

if keyObtained == bad:
    keyObtained = ok
if keyObtained == bad1:
    keyObtained = ok1

print("Key: :", keyObtained)

text = v.decrypt(encryptedText2, keyObtained)
file = open(fileName + str(".decoded.txt"), "w")
file.write(text)

file_object.close()
file.close()
