from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import sys
import datetime
import pdfkit
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from PyQt5 import QtWidgets, uic, QtCore
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
from reportlab.pdfgen import canvas
import webbrowser

app = QtWidgets.QApplication([])
dialog = uic.loadUi("pregled.ui")
global model
model = QStandardItemModel()
global mview
mview = dialog.total
mview.setModel(model)
    
def add_footer(canvas, doc):
    canvas.saveState()

    # Set dimensions for the box
    x1, y1 = 72, 50  # Left bottom corner
    x2, y2 = 522, 102  # Right top corner

    # Draw the box
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(1)
    canvas.rect(x1, y1, x2 - x1, y2 - y1)

    # Text for the footer
    footer_text = "Pacijent je blagovremeno obavešten o dijagnozi i prognozi bolesti kao i o predloženim dijagnostičkim i terapijskim procedurama. Ukratko mu je opisana predložena medicinska mera, kao i cilj i korist od predložene medicinske mere. Obavešten je i o vremenu trajanja i mogućim posledicama preduzimanja odnosno nepreduzimanja predložene medicinske mere u skladu sa Članom 28. Zakona o zdravstvenoj zaštiti."

    # Create Paragraph object for the footer text with Arial font
    style = ParagraphStyle(name="FooterStyle", fontName="Arial", fontSize=8.5)
    footer_paragraph = Paragraph(footer_text, style)

    # Set dimensions for text inside the box
    text_width, text_height = x2 - x1 - 4, y2 - y1 - 4

    # Draw the footer text inside the box
    footer_paragraph.wrap(text_width, text_height)
    footer_paragraph.drawOn(canvas, x1 + 2, y1 + 2)

    # Add short line and "Glavni direktor" text
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(0.5)
    x1_line, y1_line = x1 + 440, y1 + 70
    x2_line, y2_line = x1 + 340, y1 + 70
    canvas.line(x1_line, y1_line, x2_line, y2_line)

    glavni_direktor_text = "Dr Nataša Đorić, spec. opšte med."
    style = ParagraphStyle(name="FooterSignatureStyle", fontName="Arial", fontSize=8)
    glavni_direktor_paragraph = Paragraph(glavni_direktor_text, style)
    glavni_direktor_paragraph.wrap(200, 10)
    glavni_direktor_paragraph.drawOn(canvas, x2_line - 3, y1_line - 15)

    canvas.restoreState()




def generate_table_data(podaci):
    sum = 0
    if podaci:
        tablica_data = [['RBr', 'Analiza', 'Cena']]
        for i, podatak in enumerate(podaci, start=1):
            # Pretvori string u stvarnu listu pomoću eval()
            podatak_list = eval(podatak)
            analiza = podatak_list[0].strip()  # Ukloni nepotrebne praznine
            cena = podatak_list[1].strip().strip("']")
            sum += int(cena)
            tablica_data.append([str(i), analiza, cena])
        return tablica_data, sum
    
def generate_pdf():
    # Register Arial font
    arial_font_file = "times.ttf"
    pdfmetrics.registerFont(TTFont("Arial", arial_font_file))
    
    regular_font_path = "times.ttf"
    bold_font_path = "timesbd.ttf"
    
    pdfmetrics.registerFont(TTFont("Helvetica", regular_font_path))
    pdfmetrics.registerFont(TTFont("Helvetica-Bold", bold_font_path))
    
    registerFontFamily("Helvetica", normal="Helvetica", bold="Helvetica-Bold")
    
    styles = getSampleStyleSheet()
    
    
    imeprezime = sys.argv[1]
    rezult = imeprezime.replace(" ", "")
    
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.date.today().strftime("%d-%m-%Y")
    nazivfajla = f"{today_date}_{rezult}_Uput.pdf"
    doc = BaseDocTemplate(nazivfajla, pagesize=A4, showBoundary=0)

    
    # Calculate the height for cropping
    crop_height = 55

    # Adjust the content area to crop 100px from the bottom
    doc.bottomMargin += crop_height
    doc.height -= crop_height
    
    naslov_style = styles["Heading2"]
    naslov_style.alignment = TA_CENTER
    tekst_style = styles["Normal"]
    tekst_style.alignment = TA_CENTER

    
    logo = "logo.png"
    logo_image = Image(logo, width=70, height=73)

    naslov_firme = "Lekarska ordinacija opšte medicine"
    naziv = "HARMONY LIFE"
    adresa = "Čočetova 9/3 - 35000 Jagodina, Tel. 069/26-77-069"

    hedera_data = [[logo_image, Table([[Paragraph(naslov_firme, tekst_style)],
                                       [Paragraph(naziv, naslov_style)],
                                       [Paragraph(adresa, tekst_style)]])]]

    header_table = Table(hedera_data, colWidths=[60, doc.width - 60])
    header_table.setStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')])

    hedera = [header_table]

    hedera += [
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        Spacer(1, 1),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black')
    ]

    levo = styles["BodyText"]
    levo.alignment = TA_LEFT
    #levo.fontName = "TimesNewRoman"
    
    levo2 = styles["BodyText"]
    levo2.alignment = TA_LEFT

    
    datumrodjenja = sys.argv[2]
    danasnjidatum = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    pol = sys.argv[3]
    podaci = sys.argv[4:]
    
    data, sum = generate_table_data(podaci)
    style = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8)
    ]
    
    table = Table(data, colWidths=[20, 350, 50], style=style)
    ostatak_sadrzaja = [
        Spacer(1, 1),
        Paragraph("<b>PACIJENT:</b>", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        Paragraph(f"<b>Ime i prezime:</b> {imeprezime}", levo, encoding="utf-8"),
        Paragraph(f"<b>Datum rodjenja:</b> {datumrodjenja}", levo),
        Paragraph(f"<b>Pol: </b>  {pol}", levo),
        Paragraph(f"<b>Datum pregleda: </b>  {danasnjidatum}", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        Paragraph("<b>UPUT ZA ANALIZE</b>", naslov_style),
        Spacer(1, 5),
    ]
    

    elements = hedera + ostatak_sadrzaja

    
    # Kreiranje PageTemplate-a za footer
    footer_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='footer_frame')
    footer_template = PageTemplate(frames=[footer_frame], onPage=add_footer)

    # Povezivanje PageTemplate-a sa dokumentom
    doc.addPageTemplates(footer_template)
    elements.append(table)
    top_margin = 20
    right_margin = 10
    styles = getSampleStyleSheet()
    text_style = ParagraphStyle(
        "TextRight",
        parent=styles["Normal"],
        spaceBefore=top_margin,
        rightIndent=right_margin,
        alignment=2,
        fontSize=10,
    )
    
    your_text = f"Ukupno: {sum} din."
    elements.append(Paragraph(your_text, text_style))
    # Kreiranje PDF fajla
    doc.build(elements)
    webbrowser.open(nazivfajla)


generate_pdf()
