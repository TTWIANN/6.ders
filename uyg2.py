dosya=open("sayılar","w",encoding="utf8")
for i in range(0,10001):
    print(i)
    dosya.write(str(i)+"\n")
dosya.close()
