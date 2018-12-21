a = int(input("sayı1 :"))
b = int(input("sayı2 :"))
c = int(input("sayı3 :"))
d = int(input("sayı4 :"))
e = int(input("sayı5 :"))

dizi = [a,b,c,d,e]

dizi.sort(reverse=True)
print(dizi)
s = str(dizi)
dosya = open("E:\ogrencino_sonuc.txt","w")
dosya.write(s)
dosya.close()
