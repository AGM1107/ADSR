import PySimpleGUI as sg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from os import remove, path, rename
from pysnmp.hlapi import *

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
c.save()


def menu():
    layout = [
        [sg.Text("Sistema de Administracion de Red", font="Times-Roman 14 bold", text_color="#000",
                 justification="center", background_color="#fff")],
        [sg.Text("Practica 1 - Adquisicion de Informacion", font="Times-Roman 14 bold", text_color="#000",
                 justification="center", background_color="#fff")],
        [sg.Text("Angel Garcia Murias  2019630196", font="Times-Roman 14 bold", text_color="#000",
                 justification="center", background_color="#fff")],
        [sg.Text("Elige una opcion: ", font="Times-Roman 12", text_color="#000",
                 justification="left", background_color="#fff"), sg.InputText(background_color="#fff", border_width=0)],
        [sg.Text("1) Agregar dispositivo", font="Times-Roman 12", text_color="#000",
                 justification="left", background_color="#fff")],
        [sg.Text("2) Cambiar informacion de dispositivo", font="Times-Roman 12", text_color="#000",
                 justification="left", background_color="#fff")],
        [sg.Text("3) Eliminar dispositivo", font="Times-Roman 12", text_color="#000",
                 justification="left", background_color="#fff")],
        [sg.Text("4) Listar dispositivo", font="Times-Roman 12", text_color="#000",
                 justification="left", background_color="#fff")],
        [sg.Text("5) Salir", font="Times-Roman 12", text_color="#000",
                 justification="left", background_color="#fff")],
        [sg.Button("Aceptar")]
    ]

    window = sg.Window("Inicio", layout, margins=(80, 80), background_color="#fff")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "Aceptar":
            if values[0] == "1":
                window.close()
                layout1 = [
                    [sg.Text("Comunidad: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Text("Version SNMP: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Text("Puerto: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Text("IP: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Button("Guardar")],
                    [sg.Button("Cancelar")]
                ]

                window1 = sg.Window("Agregar dispositivo", layout1, margins=(80, 80), background_color="#fff")
                while True:
                    event, values = window1.read()
                    if event == "Exit" or event == sg.WIN_CLOSED:
                        window1.close()
                        break
                    if event == "Guardar":
                        try:
                            file = open(values[3] + "-" + values[2]+".txt", "w+")
                            file.write(values[0] + "\n" + values[1] + "\n" + values[2] + "\n" + values[3])
                            file.close()
                            print("Dispositivo guardado")
                            window1.close()
                            menu()
                        except OSError as err:
                            print("Error: {0}".format(err))
                    if event == "Cancelar":
                        window1.close()
                        menu()
                    else:
                        window1.close()
                        break
            if values[0] == "3":
                window.close()
                layout2 = [
                    [sg.Text("Puerto: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Text("IP: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Button("Eliminar")],
                    [sg.Button("Cancelar")]
                ]

                window2 = sg.Window("Eliminar dispositivo", layout2, margins=(80, 80), background_color="#fff")
                while True:
                    event, values = window2.read()
                    if event == "Exit" or event == sg.WIN_CLOSED:
                        window2.close()
                        break
                    if event == "Eliminar":
                        try:
                            if path.exists(values[1] + "-" + values[0]+".txt"):
                                remove(values[1] + "-" + values[0]+".txt")
                                print("Dispositivo eliminado")
                                window2.close()
                                menu()
                            else:
                                print("Archivo no encontrado")
                                window2.close()
                                menu()
                        except OSError as err:
                            print("Error: {0}".format(err))
                    if event == "Cancelar":
                        window2.close()
                        menu()
                    else:
                        window2.close()
                        break
            if values[0] == "2":
                window.close()
                contenido = ""
                layout3 = [
                    [sg.Text("Puerto: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Text("IP: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0)],
                    [sg.Button("Buscar")]
                ]

                window3 = sg.Window("Buscar dispositivo", layout3, margins=(80, 80), background_color="#fff")
                while True:
                    event, values = window3.read()
                    if event == "Exit" or event == sg.WIN_CLOSED:
                        window3.close()
                        break
                    if event == "Buscar":
                        try:
                            file = open(values[1] + "-" + values[0]+".txt", "r+")
                            contenido = file.read()
                            file.close()
                            window3.close()
                        except OSError as err:
                            print("Error: {0}".format(err))
                    else:
                        break
                info = contenido.split("\n")
                layout4 = [
                    [sg.Text("Comunidad: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0, default_text=info[0])],
                    [sg.Text("Version SNMP: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0, default_text=info[1])],
                    [sg.Text("Puerto: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0, default_text=info[2])],
                    [sg.Text("IP: ", font="Times-Roman 12", text_color="#000",
                             justification="left", background_color="#fff"),
                     sg.InputText(background_color="#fff", border_width=0, default_text=info[3])],
                    [sg.Button("Actualizar")],
                    [sg.Button("Cancelar")]
                ]

                window4 = sg.Window("Modificar dispositivo", layout4, margins=(80, 80), background_color="#fff")
                while True:
                    event, values = window4.read()
                    if event == "Exit" or event == sg.WIN_CLOSED:
                        window4.close()
                        break
                    if event == "Actualizar":
                        try:
                            file = open(values[3] + "-" + values[2] + ".txt", "w+")
                            file.write(values[0] + "\n" + values[1] + "\n" + values[2] + "\n" + values[3])
                            file.close()
                            if path.exists(info[3] + "-" + info[2]+".txt"):
                                rename(info[3] + "-" + info[2]+".txt", values[3] + "-" + values[2] + ".txt")
                            print("Dispositivo modificado")
                            window4.close()
                            menu()
                        except OSError as err:
                            print("Error: {0}".format(err))
                    if event == "Cancelar":
                        window4.close()
                        menu()
                    else:
                        window4.close()
                        break
            if values[0] == "4":
                window.close()
                ...;
            if values[0] == "5":
                window.close()
                break
            else:
                window.close()
                break


menu()
