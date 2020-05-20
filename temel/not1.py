#PRINT FONKSİYONU PARAMETRELERİ

YAPI
------------------------------
print(("str",int,...) , [sep =" ", file =/dosya/ya/giden/yol  flush=True or False,  end =""])

Örnek:
f = open("a","w") #file parametresi dosya açmadan çalışmaz
print('26','09','2016', sep="/" , file ="/sdcard/a.txt\" , end='')
#veriler "flush" da tutuluyor
f.close() #dosyayı kapattık böylece verilerimiz dosyaya yazıldı
Çıktı:26/09/2016. #a.txt dosyasında

Örnek:
f = open("a.txt", "w") #file parametresi dosya açmadan çalışmaz
print("26","09","2016" , sep="/" , file ="/sdcard/a.txt\",flush=True, end='')
#veriler "flush" da tutulmadan dosyaya yazıldı
f.close() #dosyayı kapattık böylece verilerimiz dosyaya yazıldı
Çıktı:26/09/2016. #a.txt dosyasında
-------------------------------
İPUÇLARI
#'*'(yıldız) işareti print fonksiyonunda şöyle kullanılabilir:
print(*'Merhaba')

Çıktı: M e r h a b a

print(*"TBMM", sep ='.')
Çıktı: T.B.M.M

#Fakat '*'(yıldız) işareti len fonksiyonu ile kullanılamaz:
>>>len('abcd')
4

>>>len(*"abcd")
Error len takes exactly one argument (4 given)

abcd yi 4\'e ayırarak len fonksiyonuna 4 ayrı argüman göndermiş oluruz

#KAÇIŞ DİZİLERİ
#----Ters Taksim(\)
>>>print("Hdjxjxjxj\
xhcjcjcjdn\
jfkcjfkckskd\
cjcjcj")

#----Yeni Satır (\n)
#----Tab boşluğu (\t)
#----Aynı Satır Başı (\r)
print(""""Merhaba\rDünya""")
Dünyaba

#----Düşey Sekme (\v)
print('Python\vDili')
Pyhton
            Dili
#----Etkisizleştirme (r) (raw)
print(r"\n,\,\t")
\n,\,\t

#----Silme (\b) (Backspace)
print("Hello World\bb)
Hello Worlb
            
#--------------------------------------------------------------------

#.format() fonksiyonu
print("{} adında, {} yaşında olan {} biri vardı".format('Ahmet', 18, 'işçi'))

