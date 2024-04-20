import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sexy_ui import *
import sqlite3

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

#veritabanı işlemleri

baglanti = sqlite3.connect("urunler.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("CREATE TABLE IF NOT EXISTS urun(urunKodu TEXT, urunAdi TEXT, birinFiyati TEXT, stokMiktari TEXT, urunAciklamasi TEXT, marka TEXT, kategori TEXT)")
baglanti.commit()

#methodlar
def kayitEkle(urun_kodu,urun_adi,birim_fiyat,stok_miktari,urun_aciklamasi,marka,kategori):
    try:
        ekle = "INSERT INTO urun(urunKodu,urunAdi,birinFiyati,stokMiktari,urunAciklamasi,marka,kategori) VALUES(?,?,?,?,?,?,?)"
        islem.execute(ekle,(urun_kodu,urun_adi,birim_fiyat,stok_miktari,urun_aciklamasi,marka,kategori))
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Ekleme İşlei Başarılı",2000)
    except Exception as error:
        ui.statusbar.showMessage("HATA! "+str(error),2000)

def kayitlariListele(tablo):
    tablo.clear()
    tablo.setHorizontalHeaderLabels("Ürün Kodu","Ürün Adi","Birim Fiyati","Stok Miktari","Ürün Açıklamasi","Marka","Kategori")

    sorgu = "SELECT * FROM urun"
    islem.execute(sorgu)

    for indexSatir,kayitNo in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNo):
            tablo.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
#buttonlar
ui.btn_ekle.clicked.connect(
                            kayitEkle(
                                    str(ui.lne_urunkodu.text()),
                                    str(ui.lne_urunadi.text()),
                                    str(ui.lne_birimfiyat.text()),
                                    str(ui.lne_stokmiktari.text()),
                                    str(ui.lne_urunaciklamasi.text()),
                                    str(ui.cmb_marka.currentText()),
                                    str(ui.cmb_kategori.currentText())
                                      )
                            )

# ui.btn_listele.clicked.connect(kayitlariListele(ui.tbl_listele))


sys.exit(uygulama.exec_())
#https://youtu.be/n5PosAYtZhg?t=2693