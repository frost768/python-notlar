import  random,sys,time
def tcno_checksum(tcno):
    if len(str(tcno)) == 9:
        tc    = '%d' % tcno
        tc10  = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
        tc10 *= 7
        tc10 -= int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
        tc10 %= 10
        tc11  = int(tc[0]) + int(tc[1]) + int(tc[2]) + int(tc[3]) + int(tc[4])
        tc11 += int(tc[5]) + int(tc[6]) + int(tc[7]) + int(tc[8]) + int(tc10)
        tc11 %= 10
        return '%s%d%d' % (tc, tc10, tc11)
    else:
        return 0

def akraba_tcno(tcno, adet):
    akraba_liste = []
    tc   = int(tcno[0:-2])
    t    = tc - 29999 * (1 + int(adet / 2))
    for i in range(adet+1):
        t += 29999
        atc = tcno_checksum(t)
        if atc == tcno:
            pass
        else:
            akraba_liste.append(atc)
    return akraba_liste[0:-1]

#################################################
def tc_check(tcno):
    toplam=0
    toplam2=0
    toplam3=0
    tc=str(tcno)
    for i in range(0,10,2):
        toplam+=int(tc[i])
        toplam2+=int(tc[i+1])
    for i in range(0,10):
        toplam3+=int(tc[i])
    toplam2-=int(tc[9])
    kat=toplam*7
    mod=(kat-toplam2)%10
    mod2=(toplam3) % 10
    if(mod==int(tc[9]) and mod2==int(tc[10])):
         print("Ok")
    else:
        print("not ok")

def tc_uret():
    a=""
    a+=str(random.randint(1,9))
    k=0
    while(k<8):
        a+=str(random.randint(0,9))
        k+=1
    toplam=0
    toplam2=0
    toplam3=0
    for l in range(0,10,2):
        toplam+=int(a[l])
    for m in range(1,9,2):
        toplam2+=int(a[m])
    kat=toplam*7
    mod=(kat-toplam2)%10
    a+=str(mod)

    for n in range(0,10):
        toplam3+=int(a[n])

    mod2=(toplam3) % 10
    a+=str(mod2)
    return int(a)
liste=akraba_tcno("tc_no",14423)
for i in liste:
    print(i)
