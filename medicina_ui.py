# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\K\Desktop\Ordinacija\medicina.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(879, 671)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.label_5.setObjectName("label_5")
        self.ImePrezime = QtWidgets.QLineEdit(Dialog)
        self.ImePrezime.setGeometry(QtCore.QRect(110, 20, 141, 20))
        self.ImePrezime.setObjectName("ImePrezime")
        self.JMBG = QtWidgets.QLineEdit(Dialog)
        self.JMBG.setGeometry(QtCore.QRect(110, 80, 141, 20))
        self.JMBG.setObjectName("JMBG")
        self.Telefon = QtWidgets.QLineEdit(Dialog)
        self.Telefon.setGeometry(QtCore.QRect(110, 110, 141, 20))
        self.Telefon.setObjectName("Telefon")
        self.Pol = QtWidgets.QComboBox(Dialog)
        self.Pol.setGeometry(QtCore.QRect(110, 140, 69, 22))
        self.Pol.setObjectName("Pol")
        self.Pol.addItem("")
        self.Pol.addItem("")
        self.DatumRodjenja = QtWidgets.QDateEdit(Dialog)
        self.DatumRodjenja.setGeometry(QtCore.QRect(110, 50, 141, 22))
        self.DatumRodjenja.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.DatumRodjenja.setObjectName("DatumRodjenja")
        self.SacuvajPacijenta = QtWidgets.QPushButton(Dialog)
        self.SacuvajPacijenta.setGeometry(QtCore.QRect(20, 212, 75, 31))
        self.SacuvajPacijenta.setObjectName("SacuvajPacijenta")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 61, 16))
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 330, 481, 281))
        self.listWidget.setObjectName("listWidget")
        self.Napomena = QtWidgets.QPlainTextEdit(Dialog)
        self.Napomena.setGeometry(QtCore.QRect(110, 170, 141, 71))
        self.Napomena.setPlainText("")
        self.Napomena.setObjectName("Napomena")
        self.IspisCekanja = QtWidgets.QListWidget(Dialog)
        self.IspisCekanja.setGeometry(QtCore.QRect(540, 50, 321, 601))
        self.IspisCekanja.setObjectName("IspisCekanja")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 251, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 290, 501, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_7.setObjectName("label_7")
        self.Refresh = QtWidgets.QPushButton(self.frame_2)
        self.Refresh.setGeometry(QtCore.QRect(10, 330, 91, 23))
        self.Refresh.setObjectName("Refresh")
        self.Pretraga = QtWidgets.QLineEdit(self.frame_2)
        self.Pretraga.setGeometry(QtCore.QRect(210, 330, 141, 20))
        self.Pretraga.setInputMask("")
        self.Pretraga.setObjectName("Pretraga")
        self.Pretrazi = QtWidgets.QPushButton(self.frame_2)
        self.Pretrazi.setGeometry(QtCore.QRect(360, 330, 131, 23))
        self.Pretrazi.setObjectName("Pretrazi")
        self.Ucitaj = QtWidgets.QPushButton(self.frame_2)
        self.Ucitaj.setGeometry(QtCore.QRect(400, 10, 91, 23))
        self.Ucitaj.setObjectName("Ucitaj")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(530, 10, 341, 651))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_8.setObjectName("label_8")
        self.Obrisi = QtWidgets.QPushButton(self.frame_3)
        self.Obrisi.setGeometry(QtCore.QRect(160, 10, 75, 23))
        self.Obrisi.setObjectName("Obrisi")
        self.OsveziCekanje = QtWidgets.QPushButton(self.frame_3)
        self.OsveziCekanje.setGeometry(QtCore.QRect(250, 10, 81, 23))
        self.OsveziCekanje.setObjectName("OsveziCekanje")
        self.saglasnost = QtWidgets.QPushButton(Dialog)
        self.saglasnost.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.saglasnost.setObjectName("saglasnost")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.ImePrezime.raise_()
        self.JMBG.raise_()
        self.Telefon.raise_()
        self.Pol.raise_()
        self.DatumRodjenja.raise_()
        self.SacuvajPacijenta.raise_()
        self.label_6.raise_()
        self.listWidget.raise_()
        self.Napomena.raise_()
        self.IspisCekanja.raise_()
        self.saglasnost.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HarmonyLife"))
        self.label.setText(_translate("Dialog", "Ime i prezime:"))
        self.label_2.setText(_translate("Dialog", "Datum rodjenja:"))
        self.label_3.setText(_translate("Dialog", "JMBG:"))
        self.label_4.setText(_translate("Dialog", "Telefon:"))
        self.label_5.setText(_translate("Dialog", "Pol:"))
        self.Pol.setItemText(0, _translate("Dialog", "Musko"))
        self.Pol.setItemText(1, _translate("Dialog", "Zensko"))
        self.DatumRodjenja.setDisplayFormat(_translate("Dialog", "d/M/yyyy"))
        self.SacuvajPacijenta.setText(_translate("Dialog", "Sacuvaj"))
        self.label_6.setText(_translate("Dialog", "Napomena:"))
        self.Napomena.setPlaceholderText(_translate("Dialog", "npr. Alergije"))
        self.label_7.setText(_translate("Dialog", "Lista pacijenata:"))
        self.Refresh.setText(_translate("Dialog", "Osvezi listu"))
        self.Pretraga.setPlaceholderText(_translate("Dialog", "npr. Pera Peric"))
        self.Pretrazi.setText(_translate("Dialog", "Pretrazi pacijenta:"))
        self.Ucitaj.setText(_translate("Dialog", "Ucitaj pacijenta"))
        self.label_8.setText(_translate("Dialog", "Lista cekanja:"))
        self.Obrisi.setText(_translate("Dialog", "Obrisi iz liste"))
        self.OsveziCekanje.setText(_translate("Dialog", "Osvezi listu"))
        self.saglasnost.setText(_translate("Dialog", "Saglasnost"))
