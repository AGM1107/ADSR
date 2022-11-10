import time
import rrdtool
from getSNMP import consultaSNMP

multicast_in = 0
paquetes_in_success = 0
sms_respuesta_icmp = 0
segments_out = 0
datagramas_in_error = 0

# 1.3.6.1.2.1       OID Base


# 1.3.6.1.2.1.2.2.1     OID grupo interfaces
# 1.3.6.1.2.1.2.2.1.buscar.interfaz     Ejemplo de uso

# .12 en interfaces in multicast (INTERFACES GROUP)
# .18 en interfaces out multicast (INTERFACES GROUP)


# 1.3.6.1.2.1.4     OID grupo IP
# 1.3.6.1.2.1.4.buscar.0        Ejemplo de uso

# .9 paquetes recibidos exitosamente (IP GROUP)
# .10 paquetes IP que los protocolos locales (IP GROUP)


# 1.3.6.1.2.1.5     OID grupo ICMP
# 1.3.6.1.2.1.5.buscar.0        Ejemplo de uso

# .22 mensajes de respuesta ICMP que ha enviado el agente (ICMP GROUP)
# .1  Mensajes ICMP que ha recibido el agente (ICMP GROUP)


# 1.3.6.1.2.1.6     OID grupo TCP
# 1.3.6.1.2.1.6.buscar.0        Ejemplo de uso

# .11 Segmentos enviados (TCP GROUP)
# .12 Segmentos retransmitidos (TCP GROUP)


# 1.3.6.1.2.1.7     OID grupo UDP
# 1.3.6.1.2.1.7.buscar.0        Ejemplo de uso

# .3 Datagramas recibidos que no pudieron ser entregados (UDP GROUP)
# .4 Datagramas enviados por el dispositivo (UDP GROUP)

while 1:
    multicast_in = int(
        consultaSNMP('comunidadSNMP', '192.168.1.79',
                     '1.3.6.1.2.1.2.2.1.12.2'))
    paquetes_in_success = int(
        consultaSNMP('comunidadSNMP', '192.168.1.79',
                     '1.3.6.1.2.1.4.9.0'))
    sms_respuesta_icmp = int(
        consultaSNMP('comunidadSNMP', '192.168.1.79',
                     '1.3.6.1.2.1.5.22.0'))
    segments_out = int(
        consultaSNMP('comunidadSNMP', '192.168.1.79',
                     '1.3.6.1.2.1.6.11.0'))
    datagramas_in_error = int(
        consultaSNMP('comunidadSNMP', '192.168.1.79',
                     '1.3.6.1.2.1.7.3.0'))

    valor = "N:" + str(multicast_in) + ':' + str(paquetes_in_success) + ':' + str(sms_respuesta_icmp) + ':' \
            + str(segments_out) + ':' + str(datagramas_in_error)
    print(valor)
    rrdtool.update('Practica2.rrd', valor)
    # rrdtool.dump('Practica2.rrd','Practica2.xml')
    time.sleep(1)

if ret:
    print(rrdtool.error())
    time.sleep(300)
