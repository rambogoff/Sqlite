# veritabanı Silme
import os
# işletim sistemi modülünü dahil ediyoruz
import sqlite3 as sql
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()

imlec.execute("DELETE FROM kitap_bilgisi WHERE okunma_durumu='hayır'")
#kitap bilgisindeki okunma_durumu hayır olanı siler

vt.commit()
# veri tabanına hafızadaki bilgiyi kaydetmek için
imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")
# ekrana listeler
vt.commit()
# veri tabanına hafızadaki bilgiyi kaydetmek için
vt.close()
# veri tabanını kapatır