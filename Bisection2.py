#Bisection 2.Soru
x1=1
x2=2
for i in range(1,5):
 denklem=(x1**3)+(4*(x1**2))-10
 denklem1=(x2**3)+(4*(x2**2))-10
 print(f"f[{x1}] fonksiyondaki degeri :",denklem)
 print(f"f[{x2}] fonksiyondaki degeri :",denklem1)
 x3=float((x1+x2)/2)
 print(f"{i}.kok tahmini:{x3}")
 denklem2=(x3**3)+(4*(x3**2))-10
 print(f"{i}. iterasyon sonucu {x3} noktasiyla elde edilen kok degeri {denklem2}")
 if denklem * denklem2<0:
      x1=x1
      x2=x3
      print(f"Kok [{x1},{x2}] arasindadir")
 elif denklem1 * denklem2<0:
           x1=x3
           x2=x2
           print(f"Kok [{x1},{x2}] arasindadir")
 
 print(f" {i}.iterasyon sonucu yeni araliklar [{x1},{x2}]")