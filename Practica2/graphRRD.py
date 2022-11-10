import sys
import rrdtool
from datetime import datetime
import time
import glob
from generatePDF import generatePDF
# tiempo_actual = int(time.time())
# Grafica desde el tiempo actual menos diez minutos
# tiempo_inicial = tiempo_actual - 1800
tiempo_creacion = datetime.strptime("10/11/2022 03:11:00", "%d/%m/%Y %H:%M:%S").timestamp()
tiempo_inicial = datetime.strptime(input("Ingresa la fecha de inicio (dd/mm/aaaa hh:mm:ss): "), "%d/%m/%Y %H:%M:%S").\
    timestamp()
if tiempo_creacion > tiempo_inicial:
    print("La fecha introducida es incorrecta")
    exit(1)

title4 = "Segmentos enviados, incluyendo los de las conexiones actuales, \n" \
         "pero excluyendo los que contienen solamente octetos retransmitidos"
title5 = "Datagramas recibidos que no pudieron ser entregados por cuestiones distintas " \
         "a la falta de aplicación en el puerto destino"

ret = rrdtool.graphv("Practica2_1.png",
                     "--start", str(tiempo_inicial)[:-2],
                     "--end", "N",
                     "--vertical-label=Paquetes",
                     "--title=Paquetes multicast que ha recibido la interfaz de red de un agente",
                     "DEF:iMulticast=Practica2.rrd:interfacesMulticast:AVERAGE",
                     "VDEF:iMulticastLast=iMulticast,LAST",
                     "VDEF:iMulticastFirst=iMulticast,FIRST",
                     "VDEF:iMulticastMax=iMulticast,MAXIMUM",
                     "CDEF:Nivel1=iMulticast,1,LT,0,iMulticast,IF",
                     "PRINT:iMulticastLast:%6.2lf",
                     "PRINT:iMulticastFirst:%6.2lf",
                     "GPRINT:iMulticastMax:%6.2lf %SegEntMAX",
                     "LINE3:iMulticast#3b83bd:Segmentros recibidos")

print(ret)

ret = rrdtool.graphv("Practica2_2.png",
                     "--start", str(tiempo_inicial)[:-2],
                     "--end", "N",
                     "--vertical-label=Paquetes",
                     "--title=Paquetes recibidos exitosamente, entregados a protocolos IP",
                     "DEF:inSuccess=Practica2.rrd:paquetesInSuccess:AVERAGE",
                     "VDEF:inSuccessLast=inSuccess,LAST",
                     "VDEF:inSuccessFirst=inSuccess,FIRST",
                     "VDEF:inSuccessMax=inSuccess,MAXIMUM",
                     "CDEF:Nivel1=inSuccess,1,LT,0,inSuccess,IF",
                     "PRINT:inSuccessLast:%6.2lf",
                     "PRINT:inSuccessFirst:%6.2lf",
                     "GPRINT:inSuccessMax:%6.2lf %SegEntMAX",
                     "LINE3:inSuccess#3b83bd:Segmentros recibidos")

print(ret)

ret = rrdtool.graphv("Practica2_3.png",
                     "--start", str(tiempo_inicial)[:-2],
                     "--end", "N",
                     "--vertical-label=Mensajes",
                     "--title=Mensajes de respuesta ICMP que ha enviado el agente",
                     "DEF:respICMP=Practica2.rrd:respuestaICMP:AVERAGE",
                     "VDEF:respICMPLast=respICMP,LAST",
                     "VDEF:respICMPFirst=respICMP,FIRST",
                     "VDEF:respICMPMax=respICMP,MAXIMUM",
                     "CDEF:Nivel1=respICMP,1,LT,0,respICMP,IF",
                     "PRINT:respICMPLast:%6.2lf",
                     "PRINT:respICMPFirst:%6.2lf",
                     "GPRINT:respICMPMax:%6.2lf %SegEntMAX",
                     "LINE3:respICMP#3b83bd:Segmentros recibidos")

print(ret)

ret = rrdtool.graphv("Practica2_4.png",
                     "--start", str(tiempo_inicial)[:-2],
                     "--end", "N",
                     "--vertical-label=Segmentos",
                     "--title="+title4,
                     "DEF:sendTCP=Practica2.rrd:segmentosTCP:AVERAGE",
                     "VDEF:sendTCPLast=sendTCP,LAST",
                     "VDEF:sendTCPFirst=sendTCP,FIRST",
                     "VDEF:sendTCPMax=sendTCP,MAXIMUM",
                     "CDEF:Nivel1=sendTCP,1,LT,0,sendTCP,IF",
                     "PRINT:sendTCPLast:%6.2lf",
                     "PRINT:sendTCPFirst:%6.2lf",
                     "GPRINT:sendTCPMax:%6.2lf %SegEntMAX",
                     "LINE3:sendTCP#3b83bd:Segmentros recibidos")

print(ret)

ret = rrdtool.graphv("Practica2_5.png",
                     "--start", str(tiempo_inicial)[:-2],
                     "--end", "N",
                     "--vertical-label=Datagramas",
                     "--title="+title5,
                     "DEF:datagramsFailed=Practica2.rrd:datagramasRecibidos:AVERAGE",
                     "VDEF:datagramsFailedLast=datagramsFailed,LAST",
                     "VDEF:datagramsFailedFirst=datagramsFailed,FIRST",
                     "VDEF:datagramsFailedMax=datagramsFailed,MAXIMUM",
                     "CDEF:Nivel1=datagramsFailed,1,LT,0,datagramsFailed,IF",
                     "PRINT:datagramsFailedLast:%6.2lf",
                     "PRINT:datagramsFailedFirst:%6.2lf",
                     "GPRINT:datagramsFailedMax:%6.2lf %SegEntMAX",
                     "LINE3:datagramsFailed#3b83bd:Segmentros recibidos")

print(ret)

generatePDF("Practica 2", "Administracion de contabilidad", glob.glob("Practica2_*.png"))
