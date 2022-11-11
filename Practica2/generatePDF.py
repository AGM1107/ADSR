from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generatePDF(nombre, titulo, data):
    w, h = letter

    c = canvas.Canvas(str(nombre) + "-AngelGM.pdf", pagesize=letter)
    c.setTitle(str(titulo))
    c.drawImage("IPN.png", 0, h - 125, width=125, height=125)
    c.drawImage("ESCOM.png", w - 125, h - 125, width=125, height=125)
    c.setFont("Times-Roman", 18)
    c.drawCentredString(w / 2, h - 100, "INSTITUTO POLITECNICO NACIONAL")
    c.setFont("Times-Roman", 16)
    c.drawCentredString(w / 2, h - 200, "ESCUELA SUPERIOR DE COMPUTO")
    c.setFont("Times-Roman", 14)
    c.drawCentredString(w / 2, h - 300, "Administracion de Servicios en Red")
    c.setFont("Times-Roman", 12)
    c.drawCentredString(w / 2, h - 400, str(titulo))
    c.drawCentredString(w / 2, h - 500, "Tanibet Perez de los Santos")
    c.drawCentredString(w / 2, h - 600, "Angel Garcia Murias")
    c.showPage()
    i = b = e = 0
    for d in data:
        if i % 2 == 0:
            c.drawImage(d, (w / 2) - 275, h - 300 - (300 * b), width=250, height=250)
            # c.drawCentredString(w / 2, h - 250, "Contacto: " + contact)
            b += 1
        else:
            c.drawImage(d, (w / 2) + 25, h - 300 - (300 * e), width=250, height=250)
            # c.drawCentredString(w / 2, h - 250, "Contacto: " + contact)
            e += 1

        if i % 2 == 1:
            c.showPage()
            b = e = 0
        i += 1
    c.save()
