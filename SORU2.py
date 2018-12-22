a = input("cümle giriniz?")
print (a[::-1])
print (a.split(" "))
harfler = []
sayisi = []
for i in(a):
    if not (i in harfler):
        harfler.append(i)
        sayisi.append(1)
    else:
        sayisi[harfler.index(i)] = sayisi[harfler.index(i)]+1
print ("her harften kac tane;")
for j in range(len(harfler)):
    print(harfler[j],"'den ",sayisi[j],"tane")
tersten = a[::-1]
ayrılmis = tersten.split(" ")
print("kendi içinde ters çevrilmiş:",ayrılmis[::-1])
unluler = ["a","e","o","ö","u","ü","ı","i"]
unlu = []
unsuz = []
for i in a:
    if i == unluler[0]or i == unluler[1]or i == unluler[2]or i == unluler[3]or i==unluler[4]or i==unluler[5]or i==unluler[6]or i==unluler[7]:
        unlu.append(i)
    else:
        unsuz.append(i)
print("ünlüharfler",unlu)
print("ünsüzharfler",unsuz)



















