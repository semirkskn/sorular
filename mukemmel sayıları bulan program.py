
toplam =0
a = int(input("sayı gir:"))
for i in range (1,a):
    if a%i==0:
        toplam+=i
if toplam==a:
    print("mukemmel sayı")
else:
    print("mukemmel ssyı degıl")
