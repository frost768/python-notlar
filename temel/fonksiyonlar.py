"""
def Fonksiyonİsmi(parametreler):
parametreler liste dict int float gibi değerleri alır
    yapılacak şeyler

Fonksiyonu cagirdik
fonksiyonismi()
"""


##########################################################################
#-----faktoriyel fonksiyonu
def fact(numara):
    fact =1
    for i in range(1,numara+1):
        fact*=i
    #print("Faktöriyel:",fact)
    return fact #fact fonksiyonundan dönen veriyi 
                #bu fonkisyon disinda kullanmak 
                #için return kullanıyoruz

#-----faktöriyel fonksiyonu

#Kullanıcı girişli
sayi = int(input("Sayi girin:"))
a=fact(sayi)
print(a)
#Kullanıcı girişli

#Direk çagirma
#fact(7)

#######################################################################


"""
Matematik dili olarak
f(x)=5x+10

#Python dili (kendim uydurdum)
def funct(x):
 x=5*x +10
 print("Sonuc:",x)

y=int(input("X="))
funct(y)
"""

#ax^2+bx+c için
def denklemkokbulma(a,b,c):
    delta=(b*b-4*a*c)
    if (delta <0):
        print("Reel kökü yok")
        return #fonksiyonun bitmesini sağlıyor
    x1=(-b - delta**0.5)/(2*a)
    x2=(-b + delta**0.5)/(2*a)
    
    return(x1,x2)

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
sonuc = denklemkokbulma(a,b,c)
if (sonuc !=None):
    print(sonuc)
