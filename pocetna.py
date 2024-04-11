from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os
import csv
import subprocess
import tkinter as tk
from tkinter import messagebox

app = QtWidgets.QApplication([])
dialog = uic.loadUi("medicina.ui")
icon_path = os.path.join(os.path.dirname(__file__), "C:\\Users\\K\\Desktop\\Ordinacija\\logo.png")  # Provide the actual path to your icon image
app_icon = QtGui.QIcon(icon_path)
app.setWindowIcon(app_icon)
dialog.show()

def sacuvaj_pacijenta():
    try:
        ime_prezime = dialog.ImePrezime.text()
        if ime_prezime=='':
            messagebox.showerror("Greška", "Greška u unosu imena i prezimena")
        datum_rodjenja = dialog.DatumRodjenja.date().toString('d-M-yyyy')
        jmbg = dialog.JMBG.text()
        if not jmbg==13:
            messagebox.showerror("Greška", "Greška u unosu JMBG")
        telefon = dialog.Telefon.text()
        pol = dialog.Pol.currentText()
        napomena = dialog.Napomena.toPlainText()

        # Kreirajte naziv foldera na osnovu imena, prezimena i datuma rođenja
        folder_naziv = f"{ime_prezime}-{datum_rodjenja}"
        folder_putanja = os.path.join(os.path.expanduser("~"), "C:\\Users\\K\Desktop\\Ordinacija\\Pacijenti", folder_naziv)

        # Proverite da li folder već postoji
        if not os.path.exists(folder_putanja):
            os.makedirs(folder_putanja)

        # Kreirajte putanju do CSV fajla
        csv_putanja = os.path.join(folder_putanja, "podaci.csv")

        # Proverite da li CSV fajl već postoji
        csv_postoji = os.path.exists(csv_putanja)
        
        pacijent = [ime_prezime, datum_rodjenja, jmbg, telefon, pol]
        
        # Upisujte podatke u CSV fajl
        with open(csv_putanja, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # Ako CSV fajl ne postoji, upišite zaglavlje
            if not csv_postoji:
                writer.writerow(["Ime i prezime", "Datum rođenja", "JMBG", "Telefon", "Pol","Napomena"])

            writer.writerow([ime_prezime, datum_rodjenja, jmbg, telefon, pol, napomena])
        # Osvežite listu pacijenata
        
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Baza.csv", "a", newline="", encoding="utf-8") as k:
            zapisnik = csv.writer(k)
            with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Baza.csv", "r", newline="", encoding="utf-8") as bus:
                citac = csv.reader(bus)
                for line in citac:
                    if pacijent == line:
                        break
                else:
                    zapisnik.writerow([ime_prezime, datum_rodjenja, jmbg, telefon, pol])
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")
def pretrazi_pacijenta():
    try:
        ime_prezime = dialog.Pretraga.text()
        dialog.listWidget.clear()
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Baza.csv", "r", newline="", encoding="utf-8") as read:
            citac = csv.reader(read)
            for line in citac:
                if ime_prezime.lower() in line[0].lower():
                    objekat = line[0] + ' - ' + line[1] + ' - ' + line[2] + ' - ' + line[3]
                    dialog.listWidget.addItem(objekat)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")
def dodaj():
    try:
        selected_item = dialog.listWidget.currentItem()
        tekst_selektovano = selected_item.text()
        delimiter = " - "
        trimmed_text = delimiter.join(tekst_selektovano.split(delimiter, 2)[:2])
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Baza.csv", "r", newline="", encoding="utf-8") as fajl:
            reader = csv.reader(fajl)
            for line in reader:
                objekt = line[0] + ' - ' + line[1]
                if objekt == trimmed_text:
                    
                    datum_rodjenja = QtCore.QDate.fromString(line[1], 'd/M/yyyy')
                    dialog.ImePrezime.setText(line[0])
                    dialog.DatumRodjenja.setDate(datum_rodjenja)
                    dialog.JMBG.setText(line[2])
                    dialog.Telefon.setText(line[3])
                    dialog.Pol.setCurrentText(line[4])
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")           

def osvezi_listu():
    try:
        dialog.listWidget.clear()
        
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Baza.csv", "r", newline="", encoding="utf-8") as read:
            citac = csv.reader(read)
            for line in citac:
                    objekat = line[0] + ' - ' + line[1] + ' - ' + line[2] + ' - ' + line[3] + ' - ' + line[4]
                    dialog.listWidget.addItem(objekat)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")
def prebaciucekanje():
    try:
        ime_prezime = dialog.ImePrezime.text()
        datum_rodjenja = dialog.DatumRodjenja.date().toString(QtCore.Qt.ISODate)
        telefon = dialog.Telefon.text()
        
        with open("C:\\Users\\K\\Desktop\\Ordinacija\\Pacijenti\\Cekanje.csv", "a", newline="", encoding="utf-8") as fajl:
            zapisnik = csv.writer(fajl)
            zapisnik.writerow([ime_prezime, datum_rodjenja, telefon])
        
        # Resetujte unos nakon čuvanja
        dialog.ImePrezime.clear()
        dialog.DatumRodjenja.setDate(QtCore.QDate.currentDate())
        dialog.JMBG.clear()
        dialog.Telefon.clear()
        dialog.Pol.setCurrentIndex(0)
        dialog.Napomena.clear()
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

def saglas(arg1,arg2,arg3):
    try:
        script2_path = "generisanjesaglasnosti.py"
        
        # Definišite argumente koje želite proslediti drugom skriptu
        args_for_script2 = [arg1, arg2, arg3]

        # Pokrenite drugi skript sa prosleđenim argumentima
        subprocess.run(["python", script2_path] + args_for_script2)
    except Exception as e:
        messagebox.showerror("Greška", "Greška u unosu")

dialog.saglasnost.clicked.connect(lambda: saglas(dialog.ImePrezime.text(), dialog.DatumRodjenja.date().toString('d/M/yyyy'), dialog.Pol.currentText()))
dialog.Ucitaj.clicked.connect(dodaj)
dialog.OsveziCekanje.clicked.connect(osvezicekanje)
dialog.Refresh.clicked.connect(osvezi_listu)
dialog.Pretrazi.clicked.connect(pretrazi_pacijenta)
dialog.SacuvajPacijenta.clicked.connect(sacuvaj_pacijenta)
dialog.SacuvajPacijenta.clicked.connect(prebaciucekanje)
dialog.Obrisi.clicked.connect(deleter)
app.exec_()
