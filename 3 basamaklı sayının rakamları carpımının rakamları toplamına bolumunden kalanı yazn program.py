a = int(input("sayı giriniz:"))
for i in range(100,1000):
    ilkrak=a//100
    ikirak=a%100//10
    ucrak=a%10

    kalan=(ilkrak*ikirak*ucrak)%(ilkrak+ikirak+ucrak)

print("kalan:",kalan)
