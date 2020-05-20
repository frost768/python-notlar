import sqlite3
import random #2.ders
import time   #2.ders
import datetime #2.ders

#VERİTABANI OLUŞTURMA
#-------------------------------------
con = sqlite3.connect("veritabani.db")
#-------------------------------------

cursor = con.cursor()

#TABLO OLUSTURMA
#---------------------------------------------------------------------------------------------------------------------
def tabloolustur():
       cursor.execute("CREATE TABLE IF NOT EXISTS tabloismi (sutun TEXT,sutun2 TEXT,sutun3 INT,sutun4 INT)")
       #               CREATE TABLE
       cursor.execute("CREATE TABLE IF NOT EXISTS tabloismi2 (zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")
#---------------------------------------------------------------------------------------------------------------------
       

#TABLOYA DEĞER EKLEME
#--------------------------------------------------------------------------
def degerekle():
    cursor.execute("INSERT INTO tabloismi VALUES ('Veri1','veri2','3','4')")
    con.commit()
    con.close()
#--------------------------------------------------------------------------


def rastgeledegerekle():
    zaman = time.time() #ANLIK ZAMAN
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime("%Y-%m-%d %H:%M:%S"))
    anahtarkelime = "Python Sqlite3" #SADECE ÖRNEK OLSUN
    deger = random.randrange(0,10) #RANDOM KÜTÜPHANESİNDEN BİR ARALIKTAN RASTGELE SEÇİM
    cursor.execute("INSERT INTO tabloismi2 (zaman,tarih,anahtarkelime,deger) VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

#10 DEĞER EKLEMEK İÇİN YAPILDI
#-------------------------------
i = 0
while (i< 10):
    rastgeledegerekle()
    #time.sleep(1) #1 sn dur

    i += 1
#-------------------------------


#VERİ OKUMA
#-------------------------------------------------------------
def degerlerial():
    cursor.execute("SELECT * FROM tabloismi WHERE sutun3 = 3")
    data = cursor.fetchall()
    print(type(data))
    for i in data:
        print(i)
#--------------------------------------------------------------

#VERİ GÜNCELLEME VE SİLME
#--------------------------------------------------------------
def silveguncelle():
        cursor.execute("SELECT * FROM tabloismi")
        data = cursor.fetchall()
        print("İlk Degerler")
        for i in data:
            print(i)
        #------------------------------------------------------------------
        #VERİ GÜNCELLEME
        cursor.execute("UPDATE tabloismi SET sutun4 = 99 WHERE sutun4 = 4")
        #------------------------------------------------------------------
        #VERİ SİLME
        cursor.execute("DELETE FROM tabloismi WHERE sutun4 = 4")
        #------------------------------------------------------------------
        cursor.execute("SELECT * FROM tabloismi")
        data = cursor.fetchall()
        print("Guncellenen Degerler")
        for i in data:
            print(i)
#--------------------------------------------------------------


""" FONKSİYONLARI ÇAĞIRMA"""
#silveguncelle()
#tabloolustur()
#degerekle()
degerlerial()

con.close()
