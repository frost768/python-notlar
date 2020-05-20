
string ="abc"
liste =["Elma","Armut","Kiraz"]
for i in string:
 print(i)
for i in liste:
 print(i)

#print(*range(baslangic,son,atlamasayisi)) 
#"*" karakteri range i bastırmak için gerekli
#print(*range(2,10,6)
#fraktal
for i in (range(10)):
 print(i*"*")

#Faktoriyel bulma
faktoriyel =1
while (True):
 print("Bir sayi girin:")
 sayi = int(input())
 for i in range(1,sayi+1):
   faktoriyel *=i
 print("Faktoriyel:",faktoriyel)
 break
  
  