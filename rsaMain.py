from Rsa import Rsa
''''
==================================
// n = 13169004533; e = 65537; y = 6029832903;
Prime  101279
130027
Fi:  13168773228
d:  72739001
 Vysledok   1234567890
==================================
// n = 1690428486610429; e = 65537; y = 22496913456008;
Prime  35352181
47816809
Fi:  1690428403441440
d:  1308297747522113
 Vysledok   1234567890
==================================
//n = 56341958081545199783; e = 65537; y = 17014716723435111315;
Prime  6940440583
8117922401
Fi:  56341958066486836800
d:  10931906232715055873
  Vysledok   1234567890
==================================
'''

print("==================================")

n1 = 13169004533
e1 = 65537
mes1 = 6029832903

r = Rsa(pN=n1, pE=e1, pY=mes1)
r.decrypt()
print("==================================")

n2 = 1690428486610429
e2 = 65537
mes2 = 22496913456008
r2 = Rsa(pN=n2, pE=e2, pY=mes2)
r2.decrypt()

print("==================================")

n3 = 56341958081545199783
e3 = 65537
mes3 = 17014716723435111315

r3 = Rsa(pN=n3, pE=e3, pY=mes3)
r3.decrypt()

print("==================================")

n4 = 6120215756887394998931731
e4 = 65537
mes4 = 5077587957348826939798388

r4 = Rsa(pN=n4, pE=e4, pY=mes4)
r4.decrypt()

print("==================================")

n5 = 514261067785300163931552303017
e5 = 65537
mes5 = 357341101854457993054768343508

r5 = Rsa(pN=n5, pE=e5, pY=mes5)
r.decrypt()

print("==================================")

n6 = 21259593755515403367535773703117421
e6 = 65537
mes6 = 18829051270422357250395121195166553

r6 = Rsa(pN=n6, pE=e6, pY=mes6)
r6.decrypt()

print("==================================")

n7 = 1371108864054663830856429909460283182291
e7 = 65537
mes7 = 35962927026249687666434209737424754460

r7 = Rsa(pN=n7, pE=e7, pY=mes7)
r7.decrypt()

print("==================================")
print("==================================")
