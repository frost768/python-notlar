#dosya = open("(dosya yolu)/dosyaadi.dosyauzantisi","r/w/a")
#r= read veri okur
#w=write dosya yoksa olusturur varsa üstüne yazar
#a=append dosya yoksa olusturur varsa ekleme yapar

#Dosya yazma
dosya = open("/sdcard/yaz.txt","w")
dosya.write("Hello World\nWhat's up?")

#Dosya Okuma
dosya = open("/sdcard/yaz.txt","r")
print(dosya.read())


#Dosyadan satır okuma
#Her satır okumadan sonra bir boşluk bırakır
dosya = open("/sdcard/yaz.txt","r")
print(dosya.readline()) #1.satır
print(dosya.readline()) #2.satır

#print(dosya.readline(sayi)) #Sayı değeri kadar karakterleri alır


#Dosyadaki satırları liste yapma
dosya = open("/sdcard/yaz.txt","r")
print(dosya.readlines())

liste = (dosya.readlines())
print(liste[0])

#Dosya bir kere açıldıktan sonra script/modül bitene kadar açık kalır
#Bu durumda dosya buffer'da yer kaplar. Bunu önlemek için
dosya.close()
#kullanılmalıdır.