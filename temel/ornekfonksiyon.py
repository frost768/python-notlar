def geometri(sekil):
    if len(sekil) == 3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        #Üçgen eşitsizligi
        if ((a+b) >c and (a+c) >b and (b+c) >a):
            if ((a==b) and (a==c) and (b==c)):
                print("Bu bir eskenar ucgendir")
            elif(a==b) or (b==c):
                print("Bu bir ikizkenar ucgen")
            else:
                print("Bu bir cesitkenar ucgen")
        else:
            print("Üçgen olusturulamaz")


    elif len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if ((a==b) and (a==c) and (a==d)):
            print("Karedir")
        elif ((a==b) and (b==c)):
            print("Dikdörtgen")
        else:
            print("Dörtgen")


    else:
        print("Hata")


while (True):
    eleman_sayisi = int(input("Eleman sayisini girin:"))
    if (eleman_sayisi == 3):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        geometri([a,b,c])

    if (eleman_sayisi == 4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        geometri([a,b,c,d])
    else:
        print("Tekrar dene")
                  
