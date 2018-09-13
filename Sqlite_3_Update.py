# veritabanı Guncelleme
import os
# işletim sistemi modülünü dahil ediyoruz
import sqlite3 as sql

veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()


imlec.execute("UPDATE kitap_bilgisi SET begeni = '****' WHERE begeni= '***'")
imlec.execute("UPDATE kitap_bilgisi SET okunma_durumu = 'evet' WHERE okunma_durumu = 'hayır'")

vt.commit()
# veri tabanına hafızadaki bilgiyi kaydetmek için

vt = sql.connect(veritabani)
imlec = vt.cursor()

imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()

print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")
# veritabanıni görüntüledik
vt.close()