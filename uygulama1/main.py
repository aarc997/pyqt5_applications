import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from main_ui import *
import sqlite3

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


#db
baglanti = sqlite3.connect("urunler.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("CREATE TABLE IF NOT EXISTS urun(urunkodu int,urunadi text, birimfiyat int, stokmiktari int, urunaciklama text, marka text, kategori text)")


def kayit_ekle():
    try:
        urunkodu = int(ui.lne_urunkodu.text())
        urunadi = ui.lne_urunadi.text()
        birimfiyati = int(ui.lne_birimfiyati.text())
        stokmiktari = int(ui.lne_stokmiktari.text())
        urunaciklamasi = ui.lne_aciklama.text()
        marka = ui.cmb_urunmarkasi.currentText()
        kategori = ui.cmb_urunkategorisi.currentText()

        ekle = "INSERT INTO urun(urunkodu,urunadi,birimfiyat,stokmiktari,urunaciklama,marka,kategori) VALUES(?,?,?,?,?,?,?)"
        islem.execute(ekle,(urunkodu,urunadi,birimfiyati,stokmiktari,urunaciklamasi,marka,kategori))
        baglanti.commit()

        ui.statusbar.showMessage("kayit ekleme başarili!",2000)
    except Exception as error:
        ui.statusbar.showMessage("HATA! "+str(error),2000)


def kayit_listele():
    ui.tbl_liste.clear()
    ui.tbl_liste.setHorizontalHeaderLabels(("ürün kodu","ürün adi","birim fiyati","stok miktari","ürün aciklamasi","marka","kategori"))
    sorgu = "select * from urun"
    islem.execute(sorgu)

    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl_liste.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kategori_listele():
    list_kat = ui.cmb_kategorilistele.currentText()
    sorgu = "select * from urun where kategori = ?"
    islem.execute(sorgu,(list_kat,))
    ui.tbl_liste.clear()

    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl_liste.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kayit_sil():
    silmsg = QMessageBox.question(pencere,"silme onayi","silmek istediğinizden emin misiniz",QMessageBox.Yes | QMessageBox.No)
    if silmsg==QMessageBox.Yes:
        seckayit = ui.tbl_liste.selectedItems()
        silkayit = seckayit[0].text()
        sorgu = "delete from urun where urunkodu = ?"
        try:
            islem.execute(sorgu,(silkayit,))
            baglanti.commit()
            kayit_listele()
            ui.statusbar.showMessage("kayit silindi",2000)
        except Exception as error:
            ui.statusbar.showMessage("HATA! "+str(error),2000)
    else:
        ui.statusbar.showMessage("silme işlemi iptal edildi",2000)

def kayit_guncelle():
    guncellemsg = QMessageBox.question(pencere,"güncelleme onayi","güncellemek istediğinizden emin misiniz",QMessageBox.Yes | QMessageBox.No)
    if guncellemsg==QMessageBox.Yes:
        seckayit = ui.tbl_liste.selectedItems()
        guncellekayit = seckayit[0].text()
        try:
            urunkodu = ui.lne_urunkodu.text()
            urunadi = ui.lne_urunadi.text()
            birimfiyat = ui.lne_birimfiyati.text()
            stokmiktari = ui.lne_stokmiktari.text()
            urunaciklama = ui.lne_aciklama.text()
            marka = ui.cmb_urunmarkasi.currentText()
            kategori = ui.cmb_urunkategorisi.currentText()


            if urunadi ==  "" and birimfiyat == "" and stokmiktari == "" and urunaciklama == "" and marka == "":
                islem.execute("update urun set katagori = ? where urunkodu = ?",(kategori,urunkodu))
            elif urunadi ==  "" and birimfiyat == "" and stokmiktari == "" and urunaciklama == "" and kategori == "":
                islem.execute("update urun set marka = ? where urunkodu = ?",(marka,urunkodu))
            elif urunadi ==  "" and birimfiyat == "" and stokmiktari == "" and marka == "" and kategori == "":
                islem.execute("update urun set urunaciklamasi = ? where urunkodu = ?",(urunaciklama,urunkodu))
            elif urunadi ==  "" and birimfiyat == "" and urunaciklama == "" and marka == "" and kategori == "":
                islem.execute("update urun set stokmiktari = ? where urunkodu = ?",(stokmiktari,urunkodu))
            elif urunadi ==  "" and stokmiktari == "" and urunaciklama == "" and marka == "" and kategori == "":
                islem.execute("update urun set birimfiyat = ? where urunkodu = ?",(birimfiyat,urunkodu))
            elif birimfiyat ==  "" and stokmiktari == "" and urunaciklama == "" and marka == "" and kategori == "":
                islem.execute("update urun set urunadi = ? where urunkodu = ?",(urunadi,urunkodu))

            else:
                islem.execute("update urun set urunadi = ? , birimfiyat = ? , stokmiktari = ? , urunaciklamasi = ? , marka = ? , katagori = ? where urunkodu = ?",(urunadi,birimfiyat,stokmiktari,urunaciklama,marka,kategori,urunkodu))
            baglanti.commit()
            kayit_listele()
            ui.statusbar.showMessage("kayit başari ile güncellendi")
        except Exception as error:
            ui.statusbar.showMessage("kayit güncellemede hata meydana geldi , hata ciktisi == "+str(error))


            if urunkodu=="" and urunadi == "" and birimfiyat=="" and stokmiktari=="" and urunaciklama == "":
                islem.execute("update urun set kategori = ? where urunkodu=?",(kategori,urunkodu))
            else:
                islem.execute("update urun set urunadi=?,birimfiyat=?,stokmiktari=?,urunaciklamasi=? where urunkodu = ?",urunadi,birimfiyat,stokmiktari,urunaciklama,marka,kategori,urunkodu)
            baglanti.commit()
            kayit_listele()
            ui.statusbar.showMessage("kayit güncellendi",2000)
        except Exception as error:
            ui.statusbar.showMessage("HATA! "+str(error),2000)



#butonlar
ui.btn_ekle.clicked.connect(kayit_ekle)
ui.btn_listele.clicked.connect(kayit_listele)
ui.btn_kategorilistele.clicked.connect(kategori_listele)
ui.btn_sil.clicked.connect(kayit_sil)
ui.btn_guncelle.clicked.connect(kayit_guncelle)


sys.exit(uygulama.exec_())