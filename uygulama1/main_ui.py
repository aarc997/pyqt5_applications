# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cmb_urunmarkasi = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_urunmarkasi.setGeometry(QtCore.QRect(10, 440, 91, 21))
        self.cmb_urunmarkasi.setObjectName("cmb_urunmarkasi")
        self.cmb_urunmarkasi.addItem("")
        self.cmb_urunmarkasi.addItem("")
        self.cmb_urunmarkasi.addItem("")
        self.cmb_urunkategorisi = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_urunkategorisi.setGeometry(QtCore.QRect(120, 440, 91, 21))
        self.cmb_urunkategorisi.setObjectName("cmb_urunkategorisi")
        self.cmb_urunkategorisi.addItem("")
        self.cmb_urunkategorisi.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 420, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 420, 81, 16))
        self.label_7.setObjectName("label_7")
        self.lne_aciklama = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_aciklama.setGeometry(QtCore.QRect(100, 220, 261, 121))
        self.lne_aciklama.setObjectName("lne_aciklama")
        self.tbl_liste = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_liste.setGeometry(QtCore.QRect(380, 100, 741, 511))
        self.tbl_liste.setRowCount(30)
        self.tbl_liste.setColumnCount(7)
        self.tbl_liste.setObjectName("tbl_liste")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 50, 141, 20))
        self.label_8.setObjectName("label_8")
        self.cmb_kategorilistele = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_kategorilistele.setGeometry(QtCore.QRect(540, 50, 131, 21))
        self.cmb_kategorilistele.setObjectName("cmb_kategorilistele")
        self.cmb_kategorilistele.addItem("")
        self.cmb_kategorilistele.addItem("")
        self.btn_kategorilistele = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kategorilistele.setGeometry(QtCore.QRect(690, 50, 75, 23))
        self.btn_kategorilistele.setObjectName("btn_kategorilistele")
        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setGeometry(QtCore.QRect(400, 640, 75, 23))
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(490, 640, 75, 23))
        self.btn_sil.setObjectName("btn_sil")
        self.btn_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guncelle.setGeometry(QtCore.QRect(580, 640, 75, 23))
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.btn_listele = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listele.setGeometry(QtCore.QRect(670, 640, 75, 23))
        self.btn_listele.setObjectName("btn_listele")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 74, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(100, 30, 135, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lne_urunkodu = QtWidgets.QLineEdit(self.widget1)
        self.lne_urunkodu.setObjectName("lne_urunkodu")
        self.verticalLayout_2.addWidget(self.lne_urunkodu)
        self.lne_urunadi = QtWidgets.QLineEdit(self.widget1)
        self.lne_urunadi.setObjectName("lne_urunadi")
        self.verticalLayout_2.addWidget(self.lne_urunadi)
        self.lne_birimfiyati = QtWidgets.QLineEdit(self.widget1)
        self.lne_birimfiyati.setObjectName("lne_birimfiyati")
        self.verticalLayout_2.addWidget(self.lne_birimfiyati)
        self.lne_stokmiktari = QtWidgets.QLineEdit(self.widget1)
        self.lne_stokmiktari.setObjectName("lne_stokmiktari")
        self.verticalLayout_2.addWidget(self.lne_stokmiktari)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmb_urunmarkasi.setCurrentIndex(-1)
        self.cmb_urunkategorisi.setCurrentIndex(-1)
        self.cmb_kategorilistele.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cmb_urunmarkasi.setItemText(0, _translate("MainWindow", "Acer"))
        self.cmb_urunmarkasi.setItemText(1, _translate("MainWindow", "Samsung"))
        self.cmb_urunmarkasi.setItemText(2, _translate("MainWindow", "Oppo"))
        self.cmb_urunkategorisi.setItemText(0, _translate("MainWindow", "telefon"))
        self.cmb_urunkategorisi.setItemText(1, _translate("MainWindow", "bilgisayar"))
        self.label_6.setText(_translate("MainWindow", "ürün markası"))
        self.label_7.setText(_translate("MainWindow", "ürün kategorisi"))
        self.label_8.setText(_translate("MainWindow", "kategoriye göre listele"))
        self.cmb_kategorilistele.setItemText(0, _translate("MainWindow", "telefon"))
        self.cmb_kategorilistele.setItemText(1, _translate("MainWindow", "bilgisayar"))
        self.btn_kategorilistele.setText(_translate("MainWindow", "Listele"))
        self.btn_ekle.setText(_translate("MainWindow", "ürün ekle"))
        self.btn_sil.setText(_translate("MainWindow", "ürün sil"))
        self.btn_guncelle.setText(_translate("MainWindow", "ürün güncelle"))
        self.btn_listele.setText(_translate("MainWindow", "ürün listele"))
        self.label.setText(_translate("MainWindow", "urun kodu"))
        self.label_2.setText(_translate("MainWindow", "urun adi"))
        self.label_3.setText(_translate("MainWindow", "birim fiyat"))
        self.label_4.setText(_translate("MainWindow", "stok miktarı"))
        self.label_5.setText(_translate("MainWindow", "ürün açıklaması"))
