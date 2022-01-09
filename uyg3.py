import time

dosya=open("files.txt","r",encoding="utf8")
icerik=dosya.read()
print("içerik yükleniyor.....")
time.sleep(2)    # 2 saniye delay getirir
print(icerik)
dosya.close()