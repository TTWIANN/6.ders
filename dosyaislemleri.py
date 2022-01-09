dosya=open("files.txt","a",encoding="utf-8") #türkçe karakter yazmka için utf-8 ekledim
#"w" kipi her zaman yeni dosya oluşturur
#"a" kipi dosya yoksa oluşturur varsa üstüne yazmaya devam eder
#"r" kipi dosyayı okumak için var dosyanın içine herhangi bişey yazamaz
dosya.write("stone ocean\n")
dosya.write("joseph\n")
dosya.write("çüöığ\n")
dosya.close()