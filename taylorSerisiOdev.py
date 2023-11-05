def faktoriyel(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact



def cos(x,n):
    N = n
    k = 0
    sonuc = 0
    while k <= N:
        if k % 2 == 0:
            isaret = 1
        else:
            isaret = -1


        term = isaret * x ** (2 * k) / faktoriyel(2 * k)
        sonuc += term
        k += 1
    return sonuc

deger=0.80901699437
pi=3.14
x=pi/5
y=cos(x,1)
print("Cos(x) fonksiyonun Taylor Serisinin tek terimini kullanarak hesaplanmış değeri:"+str(y))
kesmeHatası=deger-y
print("1.Terimin Kesme Hatası:"+str(kesmeHatası))
y=cos(x,2)
print("Cos(x) fonksiyonun Taylor Serisinin iki terimini kullanarak hesaplanmış değeri:"+str(y))
kesmeHatası=deger-y
print("2.Terimin Kesme Hatası:"+str(kesmeHatası))



