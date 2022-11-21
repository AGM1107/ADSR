import math
import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/angelgm/Angel/Servicios en Red/ADSR/6-AdministraciónDeRendimiento/RRD/'
carga_CPU = 0
total_CPU = 0
usage_RAM = 0
mem_used = 0
mem_total = 0
percent = 0.0
value = ""
# tiempo_actual = int(time.time())

while 1:
    for i in range(5, 21):
        # 1.3.6.1.2.1.25.3.3.1.2.id para la carga del procesador donde id es el identificador de cada
        # uno y el id va desde 5 hasta 20
        carga_CPU = int(consultaSNMP('comunidadSNMP', '192.168.1.167', '1.3.6.1.2.1.25.3.3.1.2.'+str(i)))
        total_CPU += carga_CPU
        value += str(carga_CPU) + ":"
        carga_CPU = 0

    total_CPU = total_CPU / 16
    # Para obtener las unidades de locacion de la RAM usada
    mem_used = int(consultaSNMP('comunidadSNMP', '192.168.1.167', '1.3.6.1.2.1.25.2.3.1.6.5'))
    # Para obtener las unidades de locacion del total de RAM
    mem_total = int(consultaSNMP('comunidadSNMP', '192.168.1.167', '1.3.6.1.2.1.25.2.3.1.5.5'))
    # Regla de 3 basica para obtener un porcentaje
    percent = ((mem_used * 100) / mem_total)
    usage_RAM = math.ceil(percent)
    # Para obtener el valor total de la RAM y la RAM usada hay que obtener el allocation_units y
    # multiplicarlo por el valor de cada una y luego dividir el resultado entre 10⁹
    valor = "N:" + str(value) + str(int(total_CPU)) + ":" + str(int(usage_RAM))
    print(valor)
    rrdtool.update(rrdpath+'monitoreo.rrd', valor)
    value = ""
    # rrdtool.dump(rrdpath+'monitoreo.rrd','monitoreo.xml')
    time.sleep(15)

if ret:
    print(rrdtool.error())
    time.sleep(300)
