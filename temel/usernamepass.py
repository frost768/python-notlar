#Bu bir yorumdur
"""
Bu bir çoklu yorumdur
"""
"""
a and b
a or b 
not a #false u true ya / true yu false a
"""
"""
defkullanici="abc"
defparola="1234"

kullanici= input("Kullanıcı Adi:")
parola = input("Parola:")

if ((defkullanici == kullanici) and (defparola == parola)):
  print("Hosgeldin %d",kullanici)

elif ((defkullanici !=kullanici) and (defparola == parola)):
  print("Kullanici adinizi mi unuttunuz?")

elif ((defkullanici == kullanici) and (parola !=defparola)):
  print("Kullanici adinizi mi unuttunuz?")

else:
 print("Tekrar deneyiniz")
"""
defkullanici="abc"
defparola="1234"

while (True):
 kullanici= input("Kullanıcı Adi:")
 parola = input("Parola:")

 if ((defkullanici == kullanici) and (defparola == parola)):
  print("Hosgeldin",kullanici)
  break

 elif ((defkullanici !=kullanici) and (defparola == parola)):
  print("Kullanici adinizi mi unuttunuz?")

 elif ((defkullanici == kullanici) and (parola !=defparola)):
  cevap = input("Parolanizi mi unuttunuz? (E/H)")
  if cevap == ("E"):
    newpass = input("Yeni parola:")
    defparola= newpass
    print("Parola degistirildi")

 else:
  print("Tekrar deneyiniz")
