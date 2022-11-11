import sys
import rrdtool
import time

last_update = rrdtool.lastupdate("Practica2.rrd")
# Grafica desde la última lectura menos cinco minutos
print(last_update)
tiempo_inicial = int(last_update['date'].timestamp())-300
print(tiempo_inicial)
rrdtool.dump("Practica2.rrd", "Practica2.xml")
result = rrdtool.fetch("Practica2.rrd", "-s,"+str(tiempo_inicial), "LAST")
start, end, step = result[0]
ds = result[1]
rows = result[2]
print(result)
print(ds)
print(rows)
