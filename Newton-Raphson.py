import math
e=math.e
x2=2
x1=1
denklem=float(4*e**(-0.5*x2)-x2)
denklem2=float(4*e**(-0.5*x1)-x1)
Raphson=1
for i in range(1,7):
    x1=x2
    x2=Raphson
    h=float(x2-x1)
    turev=float(denklem-denklem2)/(h)#türev alma
    Raphson=x2-(denklem/turev)#Raphson Formülü
    denklem3=float(4*e**(-0.5*x1)-x2)
    print(f"f[{x2}] fonksiyon degeri:",denklem3)
    print(f"{i}.iterasyon",Raphson)