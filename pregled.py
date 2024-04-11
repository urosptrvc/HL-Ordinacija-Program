from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os
import csv
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
import subprocess
from rich import get_console
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QColumnView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from bs4 import BeautifulSoup
import html2text
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QTableView, QHeaderView
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QHeaderView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtWidgets, uic, QtCore
import tkinter as tk
from tkinter import messagebox
import datetime

app = QtWidgets.QApplication([])
dialog = uic.loadUi("pregled.ui")
icon_path = os.path.join(os.path.dirname(__file__), "C:\\Users\\K\\Desktop\\Ordinacija\\logo.png")  # Provide the actual path to your icon image
app_icon = QtGui.QIcon(icon_path)
app.setWindowIcon(app_icon)
dialog.show()
global model
model = QStandardItemModel()
global mview
mview = dialog.total
mview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
mview.setModel(model)


def dodaj():
    try:
        selected_item = dialog.IspisCekanja.currentItem()
        tekst_selektovano = selected_item.text()
        delimiter = " - "
        trimmed_text = " ".join(tekst_selektovano.split(delimiter, 3)[1:3])
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Baza.csv", "r", newline="", encoding="utf-8") as fajl:
            reader = csv.reader(fajl)
            for line in reader:
                objekt = line[0] + " " + line[1]
                if objekt == trimmed_text:
                    datum_rodjenja = QtCore.QDate.fromString(line[1], QtCore.Qt.ISODate)
                    dialog.ImePrezime.setText(line[0])
                    dialog.DatumRodjenja.setDate(datum_rodjenja)
                    dialog.JMBG.setText(line[2])
                    dialog.Pol.setCurrentText(line[4])
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")
                
                
def osvezicekanje():
    try:
        dialog.IspisCekanja.clear()
        p=1
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Cekanje.csv", "r", newline="", encoding="utf-8") as read:
            citac = csv.reader(read)
            for line in citac:
                    objekat = str(p) + ' - ' + line[0] + ' - ' + line[1] + ' - ' + line[2]
                    dialog.IspisCekanja.addItem(objekat)
                    p += 1
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")
                
                
def deleter():
    try:
        selected_item = dialog.IspisCekanja.currentItem()
        dialog.IspisCekanja.takeItem(dialog.IspisCekanja.row(selected_item))
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Cekanje.csv", 'r', newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            lines = list(reader)

        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Cekanje.csv", 'w', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(lines[1:])
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

def nalazi():
    try:
        konstitucija = dialog.konstitucija.isChecked()
        grudnikops = dialog.grudnikops.isChecked()
        abdomen = dialog.abdomen.isChecked()
        ekstremiteti = dialog.ekstremiteti.isChecked()
        koza = dialog.koza.isChecked()
        kicmenistub = dialog.kicmeni.isChecked()
        pluca = dialog.pluca.isChecked()
        urogenitalni = dialog.urogenitalni.isChecked()
        stanjeglavnihcula = dialog.stanjeglavnihcula.isChecked()
        glikemija = dialog.Glikemija.isChecked()

        tekst = ""
        
        if konstitucija == True:
            tekst += "<b>Konstitucija i opšte stanje:</b> <br></br>Srednje razvijene OMG, svestan, orjentisan u vremenu, prostoru i prema ličnostima.<br></br><br></br>"
        if grudnikops == True:
            tekst += "<b>Grudni kops:</b> <br></br>Cilindričan, respiratorno pokretan.<br></br><br></br>"
        if abdomen == True:
            tekst += "<b>Abdomen:</b> <br></br>Mek, palpatorno bolno neosetljiv, jetra i slezina se ne palpiraju.<br></br><br></br>"
        if ekstremiteti == True:
            tekst += "<b>Ekstremiteti:</b> <br></br>Bez deformiteta.<br></br><br></br>"
        if koza == True:
            tekst += "<b>Koža:</b> <br></br>Uobičajene prebojenosti bez patoloških promena.<br></br><br></br>"
        if kicmenistub == True:
            tekst += "<b>Kičmeni stub:</b> <br></br>Nalaz uredan.<br></br><br></br>"
        if pluca == True:
            tekst += "<b>Pluća:</b> <br></br>Vezikularno disanje.<br></br><br></br>"
        if urogenitalni == True:
            tekst += "<b>Urogenitalni organi:</b> <br></br>Nalaz uredan.<br></br><br></br>"
        if stanjeglavnihcula == True:
            tekst += "<b>Stanje glavnih čula:</b> <br></br>Nalaz uredan.<br></br><br></br>"
        if glikemija == True:
            tekst += "<b>Glikemija:</b> <br></br>4-6 mmol/l <br></br><br></br>"
        
        dialog.IspisNalaza.setText(tekst)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

def kreiranjepdfpregleda(arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    try:
        # Definišite putanju do drugog Python skripta koji želite pokrenuti
        script2_path = "generisanjepdf.py"
        
        arg1 = dialog.IspisNalaza.toPlainText()
        # Definišite argumente koje želite proslediti drugom skriptu
        args_for_script2 = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9]

        # Pokrenite drugi skript sa prosleđenim argumentima
        subprocess.run(["python", script2_path] + args_for_script2)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

def on_tree_item_double_clicked(item):
    try:
        model.setHorizontalHeaderItem(0, QStandardItem("Naziv"))
        model.setHorizontalHeaderItem(1, QStandardItem("Cena"))
        mview.verticalHeader().setVisible(False)
        mview.setColumnWidth(0, 260)
        if item is not None:
            name_item = item.text(0)
            value_item = item.text(1)
            if name_item is not None and value_item is not None:
                model.appendRow([QStandardItem(name_item), QStandardItem(value_item)])
                dialog.total.setModel(model)
                
                
        total = 0
        for row in range(model.rowCount()):
            item = model.item(row, 1)
            if item is not None:
                total += int(item.text())
        dialog.UkupnoRacun.setText(str(total))
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")
    
def izbrisi():
    try:
        selected_indexes = mview.selectionModel().selectedRows()
        for index in reversed(selected_indexes):
            model.removeRow(index.row())
            
            
        total = 0
        for row in range(model.rowCount()):
            item = model.item(row, 1)
            if item is not None:
                total += int(item.text())
        dialog.UkupnoRacun.setText(str(total))

        # Ažuriranje prikaza QTableView
        mview.clearSelection()
        mview.reset()
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

def extract_data_from_table(table_view):
    try:
        model = table_view.model()
        data = []

        for row in range(model.rowCount(QtCore.QModelIndex())):
            row_data = []
            for column in range(model.columnCount(QtCore.QModelIndex())):
                index = model.index(row, column, QtCore.QModelIndex())
                cell_data = model.data(index, Qt.DisplayRole)
                row_data.append(cell_data)
            data.append(row_data)
        return data
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

def kreiranjeuputa(arg1,arg2,arg3,arg4):
    try:
        script2_path = "generisanjeuputa.py"
        
        # Definišite argumente koje želite proslediti drugom skriptu
        args_for_script2 = ["python", script2_path, arg1, arg2, arg3] + [str(item) for item in arg4]

        # Pokrenite drugi skript sa prosleđenim argumentima
        subprocess.run(args_for_script2)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

def covid(arg1,arg2,arg3,arg4,arg5,arg6):
    try:
        script2_path = "generisanjecovida.py"
        
        # Definišite argumente koje želite proslediti drugom skriptu
        args_for_script2 = ["python", script2_path, arg1, arg2, arg3, arg4, arg5, arg6]

        # Pokrenite drugi skript sa prosleđenim argumentima
        subprocess.run(args_for_script2)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

dialog.generisiuput.clicked.connect(lambda: kreiranjeuputa(dialog.ImePrezime.text(), dialog.DatumRodjenja.date().toString('d/M/yyyy'), dialog.Pol.currentText(), extract_data_from_table(mview)))
dialog.IzbaciLoseg.clicked.connect(izbrisi)
dialog.URINBIOHEMIJA.itemDoubleClicked.connect(on_tree_item_double_clicked)
dialog.SEROLOGIJA.itemDoubleClicked.connect(on_tree_item_double_clicked)
dialog.MIKROBIOLOGIJA.itemDoubleClicked.connect(on_tree_item_double_clicked)
dialog.MOLEKULARNA.itemDoubleClicked.connect(on_tree_item_double_clicked)
dialog.PANELI.itemDoubleClicked.connect(on_tree_item_double_clicked)
dialog.NUTRITIVNI.itemDoubleClicked.connect(on_tree_item_double_clicked)

dialog.generisiPDF.clicked.connect(lambda: kreiranjepdfpregleda("PREGLED:" if dialog.Pregled.isChecked() else "KONTROLNI PREGLED:",dialog.ImePrezime.text(), dialog.DatumRodjenja.date().toString('d/M/yyyy'), dialog.Pol.currentText(), dialog.Anamnezatxt.toPlainText(), dialog.Dijagnostika.toPlainText(), dialog.Terapija.toPlainText(), dialog.Napomene.toPlainText()))
dialog.GenerisiNalaze.clicked.connect(nalazi)
dialog.Ucitaj.clicked.connect(dodaj)
dialog.OsveziCekanje.clicked.connect(osvezicekanje)
dialog.Obrisi.clicked.connect(deleter)
dialog.GenerisiTest.clicked.connect(lambda: covid(dialog.ImePrezime.text(), dialog.DatumRodjenja.date().toString('d/M/yyyy'), dialog.Pol.currentText(), dialog.BrProtokola.text(), dialog.cbUzorak.currentText(), dialog.cbRezultat.currentText()))

dialog.URINBIOHEMIJA.setColumnWidth(0, 230)  
dialog.HORMONITUMORI.setColumnWidth(0, 230)  
dialog.SEROLOGIJA.setColumnWidth(0, 230) 
dialog.MIKROBIOLOGIJA.setColumnWidth(0, 230) 
dialog.MOLEKULARNA.setColumnWidth(0, 230) 
dialog.PANELI.setColumnWidth(0, 230) 
dialog.NUTRITIVNI.setColumnWidth(0, 230) 
app.exec_()
