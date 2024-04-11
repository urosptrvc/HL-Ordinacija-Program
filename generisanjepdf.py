from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import sys
import datetime
import pdfkit
import webbrowser

    
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
    
    
    pregled = sys.argv[2]
    imeprezime = sys.argv[3]
    asun = pregled.title()
    rezult = imeprezime.replace(" ", "")
    kraj = asun.replace(":","")
    total = kraj.replace(" ","")
    
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.date.today().strftime("%d-%m-%Y")
    global nazivfajla
    nazivfajla = f"{today_date}_{rezult}_{total}.pdf"
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

    
    nalaz = sys.argv[1]
    datumrodjenja = sys.argv[4]
    danasnjidatum = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    pol = sys.argv[5]
    anamneza = sys.argv[6]
    dijag = sys.argv[7]
    terapija = sys.argv[8]
    napomena = sys.argv[9]
    
    ostatak_sadrzaja = [
        Spacer(1, 1),
        Paragraph("<b>PACIJENT:</b>", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        Paragraph(f"<b>Ime i prezime:</b> {imeprezime}", levo, encoding="utf-8"),
        Paragraph(f"<b>Datum rodjenja:</b> {datumrodjenja}", levo),
        Paragraph(f"<b>Pol: </b>  {pol}", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        Paragraph(f"<b>{pregled}</b>", levo),
        Paragraph(f"<b>Datum pregleda: </b>  {danasnjidatum}", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        
    ]
    
    if len(anamneza)>2:
        ostatak_sadrzaja.extend([
            Paragraph("<b>ANAMNEZA: </b>", levo),
            Paragraph(f"{anamneza}", levo),
            Spacer(1, 5),
            HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        ])
    if len(nalaz)>2:
        ostatak_sadrzaja.extend([
                Paragraph("<b>NALAZ:</b>", levo),
        ])
        for paragraf_tekst in nalaz.split("\n\n"):
            try:
                nalazovi = "<b>" + paragraf_tekst.split(": ")[0] + "</b>: " + paragraf_tekst.split(": ")[1]
            except Exception as e:
                continue
            ostatak_sadrzaja.extend([
                Paragraph(f"{nalazovi}", levo2, encoding="utf-8"),
                Spacer(1, 3),
            ])
        ostatak_sadrzaja.extend([
            HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        ])
    if len(dijag)>2:
        ostatak_sadrzaja.extend([
        Paragraph("<b>DIJAGNOSTIKA:</b>", levo),
        Paragraph(f"{dijag}", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        ])
    if len(terapija)>2:   
        ostatak_sadrzaja.extend([
        Paragraph("<b>TERAPIJA:</b>", levo),
        Paragraph(f"{terapija}", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        ])
    if len(napomena)>2:     
        ostatak_sadrzaja.extend([
        Paragraph("<b>NAPOMENA:</b>", levo),
        Paragraph(f"{napomena}", levo),
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.5, lineCap='round', color='black'),
        ])

    elements = hedera + ostatak_sadrzaja

    
    # Kreiranje PageTemplate-a za footer
    footer_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='footer_frame')
    footer_template = PageTemplate(frames=[footer_frame], onPage=add_footer)

    # Povezivanje PageTemplate-a sa dokumentom
    doc.addPageTemplates(footer_template)

    # Kreiranje PDF fajla
    doc.build(elements)
    
    webbrowser.open(nazivfajla)
    


generate_pdf()