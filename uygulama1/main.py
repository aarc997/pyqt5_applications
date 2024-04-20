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

table = islem.execute("CREATE TABLE IF NOT EXISTS urun(urunKodu INT, urunAdi TEXT, birinFiyati INT, stokMiktari INT, urunAciklamasi TEXT, marka TEXT, kategori TEXT)")
baglanti.commit()






sys.exit(uygulama.exec_())