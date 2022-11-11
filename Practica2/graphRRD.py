import sys
# import rrdtool
from datetime import datetime
import time
import glob
from generatePDF import generatePDF
# tiempo_actual = int(time.time())
# Grafica desde el tiempo actual menos diez minutos
# tiempo_inicial = tiempo_actual - 1800


generatePDF("Practica2", "Administracion de contabilidad", glob.glob("Practica2_-*.png"))
