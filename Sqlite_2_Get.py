# veritabanı Sorgulama
import os
# işletim sistemi modülünü dahil ediyoruz
import sqlite3 as sql

veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()

imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
# liste halinde getiriyor
a=1
for i in kitaplar:  
    print(a," ",end="")
    for k in i:
        print(k,end=" ")
    print("")
    a=a+1

vt.close()

