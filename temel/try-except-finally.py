#try-except-finally
#Pythondaki konsol hatalarını kendi dilimizle ifade etmeye yarar
try:
   a=1
   b=0
   print(a/b)

#sıfıra bölüm hatası
except ZeroDivisionError:
     print("0'a bölüm olamaz")
finally:
#Her iki durumda da ne olursa olsun yapılacak şeyler
#dosya.close() gibi