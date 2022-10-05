import itertools

from pysnmp.hlapi import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def getinfo(oid):
    resp = ""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('comunidadSNMP', mpModel=0),
        UdpTransportTarget(('localhost', 161)),
        ContextData(),
        ObjectType(oid)
    )

    errorindication, errorstatus, errorindex, varbinds = next(iterator)

    if errorindication:
        print(errorindication)

    elif errorstatus:
        print('%s at %s' % (errorstatus.prettyPrint(),
                            errorindex and varbinds[int(errorindex) - 1][0] or '?'))

    else:
        for varBind in varbinds:
            resp = (' = '.join([x.prettyPrint() for x in varBind]))
    return resp


def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def export_to_pdf(data, c):
    c.setFont("Times-Roman", 12)
    max_rows_per_page = 25
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 25

    xlist = [x + x_offset for x in [0, 350, 250, 250, 350, 500]]
    ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                if len(str(cell)) > 40:
                    c.drawString(x + 2, y - padding + 3, str(cell)[0:40] + "...")
                else:
                    c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()


w, h = letter
c = canvas.Canvas("Practica1-AngelGM.pdf", pagesize=letter)
c.setTitle("Practica 1: SNMP")
c.drawImage("IPN.png", 0, h - 125, width=125, height=125)
c.drawImage("ESCOM.png", w - 125, h - 125, width=125, height=125)
c.setFont("Times-Roman", 18)
c.drawCentredString(w / 2, h - 100, "INSTITUTO POLITECNICO NACIONAL")
c.setFont("Times-Roman", 16)
c.drawCentredString(w / 2, h - 200, "ESCUELA SUPERIOR DE COMPUTO")
c.setFont("Times-Roman", 14)
c.drawCentredString(w / 2, h - 300, "Administracion de Servicios en Red")
c.setFont("Times-Roman", 12)
c.drawCentredString(w / 2, h - 400, "Practica 1: Adquisicion de informacion usando SNMP")
c.drawCentredString(w / 2, h - 500, "Tanibet Perez de los Santos")
c.drawCentredString(w / 2, h - 600, "Angel Garcia Murias")
c.showPage()

data = [("Interfaz", "Estatus Administrativo", "Estatus Operativo")]

res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
sysOp = res.split(" = ")[1].split(": ")[2]
res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.4.0'))
contact = res.split(" = ")[1]
res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.5.0'))
eqName = res.split(" = ")[1]
res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.6.0'))
comunity = res.split(" = ")[1]
res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.1.0'))
num = res.split(" = ")[1]

c.setFont("Times-Roman", 12)
c.drawCentredString((w / 2) - 50, h - 150, "Sistema operativo: " + sysOp)
if sysOp.__contains__("Windows"):
    c.drawImage("Windows.png", (w / 2) + 150, h - 175, width=50, height=50)
if sysOp.__contains__("Linux"):
    c.drawImage("Linux.png", (w / 2) + 150, h - 175, width=50, height=50)
if sysOp.__contains__("Mac"):
    c.drawImage("Mac.png", (w / 2) + 150, h - 175, width=50, height=50)

c.drawCentredString(w / 2, h - 250, "Contacto: " + contact)
c.drawCentredString(w / 2, h - 350, "Nombre equipo: " + eqName)
c.drawCentredString(w / 2, h - 450, "Comunidad: " + comunity)
c.drawCentredString(w / 2, h - 550, "#Interfaces: " + num)
c.showPage()

for i in range(1, int(num)):
    res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.' + str(i)))
    stA = res.split(" = ")[1]
    if stA == "1":
        stA = "Up"
    elif stA == "2":
        stA = "Down"
    else:
        stA = "Testing"
    res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.' + str(i)))
    stO = res.split(" = ")[1]
    if stO == "1":
        stO = "Up"
    elif stO == "2":
        stO = "Down"
    elif stO == "3":
        stO = "Testing"
    elif stO == "4":
        stO = "Unknown"
    elif stO == "5":
        stO = "Dormant"
    elif stO == "6":
        stO = "Not Present"
    else:
        stO = "Lower Layer Down"
    res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.' + str(i)))
    name = hex_to_string(res.split(" = ")[1])
    data.append((name, stA, stO))

export_to_pdf(data, c)
