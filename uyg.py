import datetime
dosya=open("girisler","w",encoding="utf-8")

kullanici=""
parola=""
while kullanici!="admin" or parola!="123456":
    kullanici=input("Kullanıcı adınızı giriniz: ").lower()
    parola=input("parolanızı giriniz: ")
    if kullanici=="admin" and parola=="123456":
        print("hoşgeldin")
        giris=datetime.datetime.now()
        dosya.write(str(giris))
        dosya.write("  giriş yapıldı")
    else:
        print("yanlış")
print("sisteme giriş yapıldı")