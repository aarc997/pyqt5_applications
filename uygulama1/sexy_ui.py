# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sexy-ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 91, 16))
        self.label_5.setObjectName("label_5")
        self.cmb_marka = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_marka.setGeometry(QtCore.QRect(10, 280, 121, 31))
        self.cmb_marka.setObjectName("cmb_marka")
        self.cmb_marka.addItem("")
        self.cmb_marka.addItem("")
        self.cmb_marka.addItem("")
        self.cmb_marka.addItem("")
        self.cmb_kategori = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_kategori.setGeometry(QtCore.QRect(140, 280, 121, 31))
        self.cmb_kategori.setObjectName("cmb_kategori")
        self.cmb_kategori.addItem("")
        self.cmb_kategori.addItem("")
        self.cmb_kategori.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 260, 91, 16))
        self.label_7.setObjectName("label_7")
        self.lne_urunaciklamasi = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_urunaciklamasi.setGeometry(QtCore.QRect(20, 190, 181, 61))
        self.lne_urunaciklamasi.setObjectName("lne_urunaciklamasi")
        self.tbl_listele = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_listele.setGeometry(QtCore.QRect(290, 50, 691, 551))
        self.tbl_listele.setRowCount(30)
        self.tbl_listele.setColumnCount(7)
        self.tbl_listele.setObjectName("tbl_listele")
        self.cmb_kategorilistele = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_kategorilistele.setGeometry(QtCore.QRect(400, 10, 121, 31))
        self.cmb_kategorilistele.setObjectName("cmb_kategorilistele")
        self.cmb_kategorilistele.addItem("")
        self.cmb_kategorilistele.addItem("")
        self.cmb_kategorilistele.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 20, 131, 16))
        self.label_8.setObjectName("label_8")
        self.btn_kategorilistele = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kategorilistele.setGeometry(QtCore.QRect(530, 10, 91, 31))
        self.btn_kategorilistele.setObjectName("btn_kategorilistele")
        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setGeometry(QtCore.QRect(10, 340, 91, 31))
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(10, 390, 91, 31))
        self.btn_sil.setObjectName("btn_sil")
        self.btn_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guncelle.setGeometry(QtCore.QRect(10, 440, 91, 31))
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.btn_listele = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listele.setGeometry(QtCore.QRect(10, 490, 91, 31))
        self.btn_listele.setObjectName("btn_listele")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 56, 111))
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
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(80, 20, 135, 111))
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
        self.lne_birimfiyat = QtWidgets.QLineEdit(self.widget1)
        self.lne_birimfiyat.setObjectName("lne_birimfiyat")
        self.verticalLayout_2.addWidget(self.lne_birimfiyat)
        self.lne_stokmiktari = QtWidgets.QLineEdit(self.widget1)
        self.lne_stokmiktari.setObjectName("lne_stokmiktari")
        self.verticalLayout_2.addWidget(self.lne_stokmiktari)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmb_marka.setCurrentIndex(-1)
        self.cmb_kategori.setCurrentIndex(-1)
        self.cmb_kategorilistele.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "ürün açıklaması"))
        self.cmb_marka.setItemText(0, _translate("MainWindow", "Acer"))
        self.cmb_marka.setItemText(1, _translate("MainWindow", "Samsung"))
        self.cmb_marka.setItemText(2, _translate("MainWindow", "Apple"))
        self.cmb_marka.setItemText(3, _translate("MainWindow", "Oppo"))
        self.cmb_kategori.setItemText(0, _translate("MainWindow", "Telefon"))
        self.cmb_kategori.setItemText(1, _translate("MainWindow", "Bilgisayar"))
        self.cmb_kategori.setItemText(2, _translate("MainWindow", "Beyaz Eşya"))
        self.label_6.setText(_translate("MainWindow", "ürün markası"))
        self.label_7.setText(_translate("MainWindow", "ürün kategorisi"))
        self.cmb_kategorilistele.setItemText(0, _translate("MainWindow", "Telefon"))
        self.cmb_kategorilistele.setItemText(1, _translate("MainWindow", "Bilgisayar"))
        self.cmb_kategorilistele.setItemText(2, _translate("MainWindow", "Beyaz Eşya"))
        self.label_8.setText(_translate("MainWindow", "kategoriye göre listele"))
        self.btn_kategorilistele.setText(_translate("MainWindow", "listele"))
        self.btn_ekle.setText(_translate("MainWindow", "Ürün Ekle"))
        self.btn_sil.setText(_translate("MainWindow", "Ürün Sil"))
        self.btn_guncelle.setText(_translate("MainWindow", "Ürün Güncelle"))
        self.btn_listele.setText(_translate("MainWindow", "Ürün listele"))
        self.label.setText(_translate("MainWindow", "ürün kodu"))
        self.label_2.setText(_translate("MainWindow", "ürün adı"))
        self.label_3.setText(_translate("MainWindow", "birim fiyat"))
        self.label_4.setText(_translate("MainWindow", "stok miktarı"))
