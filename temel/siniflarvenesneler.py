#1.DERS

class Dusman:
    kalan_can = 3
    def saldir(self):
        print("Hücuuum")
        self.kalan_can -=1
    def hayatta_mi(self):
        if (self.kalan_can<=0):
            print("Öldü")
        else:
            print(str(self.kalan_can)  + " canım kaldı")

dusman1 = Dusman()
dusman2 = Dusman()

dusman1.saldir() #Hücuum
dusman1.saldir() #Hücuum
dusman1.hayatta_mi() #1 canım kaldı

dusman2.saldir() #Hücuum
dusman2.saldir() #Hücuum
dusman2.saldir() #Hücuum
dusman2.hayatta_mi() #Öldü


#-------------------------------------------

#2.DERS

class Dusman:
    def __init__(self,
                 #prmtr = varsayılan deger
                 isim = "Dusman",
                 kalan_can = "500",
                 saldiri_gucu = "1000",
                 mermi_sayisi = "120"):
        #__init__, Dusman class ına parametre verebilmemizi sağlıyor
        
        self.isim = isim #self. koymamızın nedeni
        self.kalan_can = kalan_can #bu variable ların Dusman class ına
        self.saldiri_gucu = saldiri_gucu #ait olduğunu göstermek
        self.mermi_sayisi = mermi_sayisi

    def print(self):
        print("Basılıyor...")
        print("İsim: ",self.isim,
              "Kalan Can: ",self.kalan_can,
              "Saldırı Gücü: ",self.saldiri_gucu,
              "Mermi Sayısı: ",self.mermi_sayisi)

#Özelleştirilmiş objeler
dusman1 = Dusman("Ali",2000,30,50)
dusman2 = Dusman("Veli",1000,20,40)
#------------------------------------

dusman3 = Dusman()

print("Dusman1 ----------------------------")
dusman1.print()

print("Dusman2 ----------------------------")
dusman2.print()

#Varsayılan Degerleri Kullanan Obje#
print("Dusman3 -----------------------------")
dusman3.print()

#-----------------------------------------------------------------------

#3.DERS
"""
import random
class Dusman:
    def __init__(self,
                 #prmtr = varsayılan deger
                 isim = "Dusman",
                 kalan_can = "500",
                 saldiri_gucu = "1000",
                 mermi_sayisi = "120"):
        #init, Dusman class ına parametre verebilmemizi sağlıyor
        
        self.isim = isim #self. koymamızın nedeni
        self.kalan_can = kalan_can #bu variable ların Dusman class ına
        self.saldiri_gucu = saldiri_gucu #ait olduğunu göstermek
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + " Saldırıyor")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi) + " kadar harcandi")
        self.mermi_sayisi -= harcanan_mermi

        return(harcanan_mermi,self.saldiri_gucu)

    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print("Vuruldum")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermi_bitti_mi(self):
        if (self.mermi_sayisi <= 0 ):
            print(self.isim + " konuşuyor : Mermim bitti.")
            return True
        return False

    def hayatta_mi(self):
        if (self.kalan_can <=0):
            print("ölüyoruuuum...")

    def print(self):
        print("Basılıyor...")
        print("İsim: ",self.isim,
              "Kalan Can: ",self.kalan_can,
              "Saldırı Gücü: ",self.saldiri_gucu,
              "Mermi Sayısı: ",self.mermi_sayisi)

dusmanlar = []

i = 0
while (i < 2):
    rastgelecan = random.randrange(100,200)
    rastgelesaldirigucu = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i += i

for dusman in dusmanlar:
    dusman.print()
"""
#------------------------------------------------------

#4.DERS
"""
import random
class Dusman:
    def __init__(self,
                 #prmtr = varsayılan deger
                 isim = "Dusman",
                 kalan_can = "500",
                 saldiri_gucu = "1000",
                 mermi_sayisi = "120"):
        #init özel Dusman class ına parametre verebilmemizi sağlıyor
        
        self.isim = isim #self. koymamızın nedeni
        self.kalan_can = kalan_can #bu variable ların Dusman class ına
        self.saldiri_gucu = saldiri_gucu #ait olduğunu göstermek
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + " Saldırıyor")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi) + " kadar harcandi")
        self.mermi_sayisi -= harcanan_mermi

        return(harcanan_mermi,self.saldiri_gucu)

    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print("Vuruldum")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermi_bitti_mi(self):
        if (self.mermi_sayisi <= 0 ):
            print(self.isim + " konuşuyor : Mermim bitti.")
            return True
        return False

    def hayatta_mi(self):
        if (self.kalan_can <=0):
            print("ölüyoruuuum...")

    def print(self):
        print("Basılıyor...")
        print("İsim: ",self.isim,
              "Kalan Can: ",self.kalan_can,
              "Saldırı Gücü: ",self.saldiri_gucu,
              "Mermi Sayısı: ",self.mermi_sayisi)

dusmanlar = []
i = 0
while (i <5):
    rastgelecan = random.randrange(100,200)
    rastgelesaldirigucu = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i += i

print(dusmanlar)

i = 0
while(1 < 3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldir()

    dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])

    print("Round bitti...")

    i += i
"""
