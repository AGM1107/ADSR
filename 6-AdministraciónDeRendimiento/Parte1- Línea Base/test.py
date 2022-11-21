import math
import time

from getSNMP import consultaSNMP

mem_used = 0
mem_total = 0
allocation_units = 0
percent = 0.0

while 1:
    mem_used = int(consultaSNMP('comunidadSNMP', '192.168.1.167', '1.3.6.1.2.1.25.2.3.1.6.5'))
    mem_total = int(consultaSNMP('comunidadSNMP', '192.168.1.167', '1.3.6.1.2.1.25.2.3.1.5.5'))
    allocation_units = int(consultaSNMP('comunidadSNMP', '192.168.1.167', '1.3.6.1.2.1.25.2.3.1.4.5'))
    percent = ((mem_used * 100) / mem_total)

    print("Memoria usada: " + str((mem_used * allocation_units) / (10 ** 9)))
    print("Memoria total: " + str((mem_total * allocation_units) / (10 ** 9)))
    print("Porcentaje utilizado directo: " + str(math.ceil(percent)))
    time.sleep(5)
