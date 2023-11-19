#Bisection 1.Soru
x1=2#alt kök
x2=4#üst kök
for i in range(1,5):
 denklem=(x1**3)-(2*(x1**2))-5
 denklem1=(x2**3)-(2*(x2**2))-5
 print(f"f[{x1}] fonksiyondaki degeri :",denklem)
 print(f"f[{x2}] fonksiyondaki degeri :",denklem1)
 x3=float((x1+x2)/2)#orta kök
 print(f"{i}.kok tahmini:{x3}")
 denklem2=(x3**3)-(2*(x3**2))-5 
 print(f" {i}. iterasyon sonucu {x3} noktasiyla elde edilen kok degeri {denklem2}")
 if denklem * denklem2<0:
      x1=x1#alt kök aynı kaldı
      x2=x3# x3 ü üst köke attık
      print(f"Kok [{x1},{x2}] arasindadir")
 elif denklem1 * denklem2<0:
           x1=x3#x3 ü alt köke attık
           x2=x2#üst kök aynı kaldı
           print(f"Kok [{x1},{x2}] arasindadir")

print(f" {i}.iterasyon sonucu yeni araliklar [{x1},{x2}]")