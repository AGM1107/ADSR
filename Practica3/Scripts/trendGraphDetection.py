import rrdtool
from Notify import send_alert_attached
import time
from getInfo import getinfo
from pysnmp.hlapi import *

rrdpath = '//home/angelgm/Angel/Servicios en Red/ADSR/Practica3/RRD/'
imgpath = '/home/angelgm/Angel/Servicios en Red/ADSR/Practica3/IMG/'

res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
sysOp = res.split(" = ")[1].split(": ")[2]

res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.4.0'))
contact = res.split(" = ")[1]

res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.5.0'))
eqName = res.split(" = ")[1]

bodyText = "Sistema operativo: " + sysOp + "\n" + "Nombre equipo: " + eqName + "\n" + "Contacto: " + contact

def generarGrafica(ultima_lectura, primera_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = primera_lectura
    ret = rrdtool.graphv(imgpath + "cpuload.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=CPU load",
                         "--lower-limit", "0",
                         "--upper-limit", "100",
                         "--title=Carga de cada procesador y el promedio de todos",
                         "DEF:cargaCPU1=" + rrdpath + "monitoreo.rrd:CPUload1:AVERAGE",
                         "VDEF:cargaMAX1=cargaCPU1,MAXIMUM",
                         "VDEF:cargaMIN1=cargaCPU1,MINIMUM",
                         # "VDEF:cargaSTDEV1=cargaCPU1,STDEV",
                         "VDEF:cargaLAST1=cargaCPU1,LAST",
                         "LINE1:cargaCPU1#FF0000:Carga del CPU 1",
                         "PRINT:cargaLAST1:%6.2lf",
                         "GPRINT:cargaMIN1:%6.2lf %SMIN",
                         "GPRINT:cargaMAX1:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV1:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST1:%6.2lf %SLAST",
                         "DEF:cargaCPU2=" + rrdpath + "monitoreo.rrd:CPUload2:AVERAGE",
                         "VDEF:cargaMAX2=cargaCPU2,MAXIMUM",
                         "VDEF:cargaMIN2=cargaCPU2,MINIMUM",
                         # "VDEF:cargaSTDEV2=cargaCPU2,STDEV",
                         "VDEF:cargaLAST2=cargaCPU2,LAST",
                         "LINE1:cargaCPU2#FFFF00:Carga del CPU 2",
                         "PRINT:cargaLAST2:%6.2lf",
                         "GPRINT:cargaMIN2:%6.2lf %SMIN",
                         "GPRINT:cargaMAX2:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV2:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST2:%6.2lf %SLAST",
                         "DEF:cargaCPU3=" + rrdpath + "monitoreo.rrd:CPUload3:AVERAGE",
                         "VDEF:cargaMAX3=cargaCPU3,MAXIMUM",
                         "VDEF:cargaMIN3=cargaCPU3,MINIMUM",
                         # "VDEF:cargaSTDEV3=cargaCPU3,STDEV",
                         "VDEF:cargaLAST3=cargaCPU3,LAST",
                         "LINE1:cargaCPU3#00FF00:Carga del CPU 3",
                         "PRINT:cargaLAST3:%6.2lf",
                         "GPRINT:cargaMIN3:%6.2lf %SMIN",
                         "GPRINT:cargaMAX3:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV3:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST3:%6.2lf %SLAST",
                         "DEF:cargaCPU4=" + rrdpath + "monitoreo.rrd:CPUload4:AVERAGE",
                         "VDEF:cargaMAX4=cargaCPU4,MAXIMUM",
                         "VDEF:cargaMIN4=cargaCPU4,MINIMUM",
                         # "VDEF:cargaSTDEV4=cargaCPU4,STDEV",
                         "VDEF:cargaLAST4=cargaCPU4,LAST",
                         "LINE1:cargaCPU4#808080:Carga del CPU 4",
                         "PRINT:cargaLAST4:%6.2lf",
                         "GPRINT:cargaMIN4:%6.2lf %SMIN",
                         "GPRINT:cargaMAX4:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV4:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST4:%6.2lf %SLAST",
                         "DEF:cargaCPU5=" + rrdpath + "monitoreo.rrd:CPUload5:AVERAGE",
                         "VDEF:cargaMAX5=cargaCPU5,MAXIMUM",
                         "VDEF:cargaMIN5=cargaCPU5,MINIMUM",
                         # "VDEF:cargaSTDEV5=cargaCPU5,STDEV",
                         "VDEF:cargaLAST5=cargaCPU5,LAST",
                         "LINE1:cargaCPU5#0000FF:Carga del CPU 5",
                         "PRINT:cargaLAST5:%6.2lf",
                         "GPRINT:cargaMIN5:%6.2lf %SMIN",
                         "GPRINT:cargaMAX5:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV5:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST5:%6.2lf %SLAST",
                         "DEF:cargaCPU6=" + rrdpath + "monitoreo.rrd:CPUload6:AVERAGE",
                         "VDEF:cargaMAX6=cargaCPU6,MAXIMUM",
                         "VDEF:cargaMIN6=cargaCPU6,MINIMUM",
                         # "VDEF:cargaSTDEV6=cargaCPU6,STDEV",
                         "VDEF:cargaLAST6=cargaCPU6,LAST",
                         "LINE1:cargaCPU6#FF00FF:Carga del CPU 6",
                         "PRINT:cargaLAST6:%6.2lf",
                         "GPRINT:cargaMIN6:%6.2lf %SMIN",
                         "GPRINT:cargaMAX6:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV6:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST6:%6.2lf %SLAST",
                         "DEF:cargaCPU7=" + rrdpath + "monitoreo.rrd:CPUload7:AVERAGE",
                         "VDEF:cargaMAX7=cargaCPU7,MAXIMUM",
                         "VDEF:cargaMIN7=cargaCPU7,MINIMUM",
                         # "VDEF:cargaSTDEV7=cargaCPU7,STDEV",
                         "VDEF:cargaLAST7=cargaCPU7,LAST",
                         "LINE1:cargaCPU7#800080:Carga del CPU 7",
                         "PRINT:cargaLAST7:%6.2lf",
                         "GPRINT:cargaMIN7:%6.2lf %SMIN",
                         "GPRINT:cargaMAX7:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV7:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST7:%6.2lf %SLAST",
                         "DEF:cargaCPU8=" + rrdpath + "monitoreo.rrd:CPUload8:AVERAGE",
                         "VDEF:cargaMAX8=cargaCPU8,MAXIMUM",
                         "VDEF:cargaMIN8=cargaCPU8,MINIMUM",
                         # "VDEF:cargaSTDEV8=cargaCPU8,STDEV",
                         "VDEF:cargaLAST8=cargaCPU8,LAST",
                         "LINE1:cargaCPU8#808000:Carga del CPU 8",
                         "PRINT:cargaLAST8:%6.2lf",
                         "GPRINT:cargaMIN8:%6.2lf %SMIN",
                         "GPRINT:cargaMAX8:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV8:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST8:%6.2lf %SLAST",
                         "DEF:cargaCPU9=" + rrdpath + "monitoreo.rrd:CPUload9:AVERAGE",
                         "VDEF:cargaMAX9=cargaCPU9,MAXIMUM",
                         "VDEF:cargaMIN9=cargaCPU9,MINIMUM",
                         # "VDEF:cargaSTDEV9=cargaCPU9,STDEV",
                         "VDEF:cargaLAST9=cargaCPU9,LAST",
                         "LINE1:cargaCPU9#800000:Carga del CPU 9",
                         "PRINT:cargaLAST9:%6.2lf",
                         "GPRINT:cargaMIN9:%6.2lf %SMIN",
                         "GPRINT:cargaMAX9:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV9:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST9:%6.2lf %SLAST",
                         "DEF:cargaCPU10=" + rrdpath + "monitoreo.rrd:CPUload10:AVERAGE",
                         "VDEF:cargaMAX10=cargaCPU10,MAXIMUM",
                         "VDEF:cargaMIN10=cargaCPU10,MINIMUM",
                         # "VDEF:cargaSTDEV10=cargaCPU10,STDEV",
                         "VDEF:cargaLAST10=cargaCPU10,LAST",
                         "LINE1:cargaCPU10#C0C0C0:Carga del CPU 10",
                         "PRINT:cargaLAST10:%6.2lf",
                         "GPRINT:cargaMIN10:%6.2lf %SMIN",
                         "GPRINT:cargaMAX10:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV10:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST10:%6.2lf %SLAST",
                         "DEF:cargaCPU11=" + rrdpath + "monitoreo.rrd:CPUload11:AVERAGE",
                         "VDEF:cargaMAX11=cargaCPU11,MAXIMUM",
                         "VDEF:cargaMIN11=cargaCPU11,MINIMUM",
                         # "VDEF:cargaSTDEV11=cargaCPU11,STDEV",
                         "VDEF:cargaLAST11=cargaCPU11,LAST",
                         "LINE1:cargaCPU11#FA8072:Carga del CPU 11",
                         "PRINT:cargaLAST11:%6.2lf",
                         "GPRINT:cargaMIN11:%6.2lf %SMIN",
                         "GPRINT:cargaMAX11:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV11:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST11:%6.2lf %SLAST",
                         "DEF:cargaCPU12=" + rrdpath + "monitoreo.rrd:CPUload12:AVERAGE",
                         "VDEF:cargaMAX12=cargaCPU12,MAXIMUM",
                         "VDEF:cargaMIN12=cargaCPU12,MINIMUM",
                         # "VDEF:cargaSTDEV12=cargaCPU12,STDEV",
                         "VDEF:cargaLAST12=cargaCPU12,LAST",
                         "LINE1:cargaCPU12#BA4A00:Carga del CPU 12",
                         "PRINT:cargaLAST12:%6.2lf",
                         "GPRINT:cargaMIN12:%6.2lf %SMIN",
                         "GPRINT:cargaMAX12:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV12:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST12:%6.2lf %SLAST",
                         "DEF:cargaCPU13=" + rrdpath + "monitoreo.rrd:CPUload13:AVERAGE",
                         "VDEF:cargaMAX13=cargaCPU13,MAXIMUM",
                         "VDEF:cargaMIN13=cargaCPU13,MINIMUM",
                         # "VDEF:cargaSTDEV13=cargaCPU13,STDEV",
                         "VDEF:cargaLAST13=cargaCPU13,LAST",
                         "LINE1:cargaCPU13#7D6608:Carga del CPU 13",
                         "PRINT:cargaLAST13:%6.2lf",
                         "GPRINT:cargaMIN13:%6.2lf %SMIN",
                         "GPRINT:cargaMAX13:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV13:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST13:%6.2lf %SLAST",
                         "DEF:cargaCPU14=" + rrdpath + "monitoreo.rrd:CPUload14:AVERAGE",
                         "VDEF:cargaMAX14=cargaCPU14,MAXIMUM",
                         "VDEF:cargaMIN14=cargaCPU14,MINIMUM",
                         # "VDEF:cargaSTDEV14=cargaCPU14,STDEV",
                         "VDEF:cargaLAST14=cargaCPU14,LAST",
                         "LINE1:cargaCPU14#1B2631:Carga del CPU 14",
                         "PRINT:cargaLAST14:%6.2lf",
                         "GPRINT:cargaMIN14:%6.2lf %SMIN",
                         "GPRINT:cargaMAX14:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV14:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST14:%6.2lf %SLAST",
                         "DEF:cargaCPU15=" + rrdpath + "monitoreo.rrd:CPUload15:AVERAGE",
                         "VDEF:cargaMAX15=cargaCPU15,MAXIMUM",
                         "VDEF:cargaMIN15=cargaCPU15,MINIMUM",
                         # "VDEF:cargaSTDEV15=cargaCPU15,STDEV",
                         "VDEF:cargaLAST15=cargaCPU15,LAST",
                         "LINE1:cargaCPU15#BB8FCE:Carga del CPU 15",
                         "PRINT:cargaLAST15:%6.2lf",
                         "GPRINT:cargaMIN15:%6.2lf %SMIN",
                         "GPRINT:cargaMAX15:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV15:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST15:%6.2lf %SLAST",
                         "DEF:cargaCPU16=" + rrdpath + "monitoreo.rrd:CPUload16:AVERAGE",
                         "VDEF:cargaMAX16=cargaCPU16,MAXIMUM",
                         "VDEF:cargaMIN16=cargaCPU16,MINIMUM",
                         # "VDEF:cargaSTDEV16=cargaCPU16,STDEV",
                         "VDEF:cargaLAST16=cargaCPU16,LAST",
                         "LINE1:cargaCPU16#E6B0AA:Carga del CPU 16",
                         "PRINT:cargaLAST16:%6.2lf",
                         "GPRINT:cargaMIN16:%6.2lf %SMIN",
                         "GPRINT:cargaMAX16:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV16:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST16:%6.2lf %SLAST",
                         "DEF:cargaCPU=" + rrdpath + "monitoreo.rrd:CPUload:AVERAGE",
                         "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                         "VDEF:cargaMIN=cargaCPU,MINIMUM",
                         # "VDEF:cargaSTDEV=cargaCPU,STDEV",
                         "VDEF:cargaLAST=cargaCPU,LAST",
                         "CDEF:umbral35=cargaCPU,35,LT,0,cargaCPU,IF",
                         "CDEF:umbral40=cargaCPU,40,LT,0,cargaCPU,IF",
                         "CDEF:umbral45=cargaCPU,45,LT,0,cargaCPU,IF",
                         "LINE1:cargaCPU#00FFFF:Carga promedio del CPU",
                         # "AREA:umbral15#FF9F00:Carga CPU mayor de 15",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaMAX:%6.2lf %SMAX",
                         # "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST",
                         "HRULE:35#FF0000:Umbral  35%",
                         "HRULE:40#00FF00:Umbral  40%",
                         "HRULE:45#0000FF:Umbral  45%")
    print(ret)

    ret = rrdtool.graphv(imgpath + "ramusage.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=RAM usage",
                         "--lower-limit", "0",
                         "--upper-limit", "100",
                         "--title=Uso de la memoria RAM en %",
                         "DEF:usageRAM=" + rrdpath + "monitoreo.rrd:RAMusage:AVERAGE",
                         "VDEF:RAMMAX=usageRAM,MAXIMUM",
                         "VDEF:RAMMIN=usageRAM,MINIMUM",
                         "VDEF:RAMSTDEV=usageRAM,STDEV",
                         "VDEF:RAMLAST=usageRAM,LAST",
                         "CDEF:umbral75=usageRAM,75,LT,0,usageRAM,IF",
                         "CDEF:umbral80=usageRAM,80,LT,0,usageRAM,IF",
                         "CDEF:umbral85=usageRAM,85,LT,0,usageRAM,IF",
                         "AREA:usageRAM#00FFFF:Uso de RAM",
                         # "AREA:umbral15#FF9F00:Carga CPU mayor de 15",
                         "PRINT:RAMLAST:%6.2lf",
                         "GPRINT:RAMMIN:%6.2lf %SMIN",
                         "GPRINT:RAMMAX:%6.2lf %SMAX",
                         # "GPRINT:RAMSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:RAMLAST:%6.2lf %SLAST",
                         "HRULE:75#FF0000:Umbral  75%",
                         "HRULE:80#00FF00:Umbral  80%",
                         "HRULE:85#0000FF:Umbral  85%",)
    print(ret)

    ret = rrdtool.graphv(imgpath + "traficored.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Trafico de Red",
                         "--title=Uso de la Red",
                         "DEF:traficoIn=" + rrdpath + "monitoreo.rrd:InOctets:AVERAGE",
                         "VDEF:traficoInMax=traficoIn,MAXIMUM",
                         "VDEF:traficoInMin=traficoIn,MINIMUM",
                         "VDEF:traficoInSTD=traficoIn,STDEV",
                         "VDEF:traficoInLast=traficoIn,LAST",
                         "LINE2:traficoIn#00FFFF:Trafico Entrada",
                         "PRINT:traficoInLast:%6.2lf",
                         "GPRINT:traficoInMin:%6.2lf %SMIN",
                         "GPRINT:traficoInMax:%6.2lf %SMAX",
                         # "GPRINT:traficoInSTD:%6.2lf %SSTDEV",
                         "GPRINT:traficoInLast:%6.2lf %SLAST",
                         "DEF:traficoOut=" + rrdpath + "monitoreo.rrd:OutOctets:AVERAGE",
                         "VDEF:traficoOutMax=traficoOut,MAXIMUM",
                         "VDEF:traficoOutMin=traficoOut,MINIMUM",
                         "VDEF:traficoOutSTD=traficoOut,STDEV",
                         "VDEF:traficoOutLast=traficoOut,LAST",
                         "LINE2:traficoOut#FF00FF:Trafico Salida",
                         "PRINT:traficoOutLast:%6.2lf",
                         "GPRINT:traficoOutMin:%6.2lf %SMIN",
                         "GPRINT:traficoOutMax:%6.2lf %SMAX",
                         # "GPRINT:traficoOutSTD:%6.2lf %SSTDEV",
                         "GPRINT:traficoOutLast:%6.2lf %SLAST")
    print(ret)


while 1:
    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "monitoreo.rrd")
    primera_actualizacion = rrdtool.first(rrdpath + "monitoreo.rrd")
    timestampf = ultima_actualizacion['date'].timestamp()
    timestampi = primera_actualizacion
    dato_CPU = ultima_actualizacion['ds']["CPUload"]
    dato_RAM = ultima_actualizacion['ds']["RAMusage"]

    if 35 <= dato_CPU < 40:
        generarGrafica(int(timestampf), int(timestampi))
        send_alert_attached("CPU sobrepasa el primer umbral", "cpuload", bodyText)
        print("CPU sobrepasa el primer umbral")
    elif 40 <= dato_CPU < 45:
        generarGrafica(int(timestampf), int(timestampi))
        send_alert_attached("CPU sobrepasa el segundo umbral", "cpuload", bodyText)
        print("CPU sobrepasa el segundo umbral")
    elif dato_CPU >= 45:
        generarGrafica(int(timestampf), int(timestampi))
        send_alert_attached("CPU sobrepasa el tercer umbral", "cpuload", bodyText)
        print("CPU sobrepasa el tercer umbral")

    print(dato_RAM)
    if 75 <= dato_RAM < 80:
        generarGrafica(int(timestampf), int(timestampi))
        send_alert_attached("RAM sobrepasa el primer umbral", "ramusage", bodyText)
        print("RAM sobrepasa el primer umbral")
        break
    elif 80 <= dato_RAM < 85:
        generarGrafica(int(timestampf), int(timestampi))
        send_alert_attached("RAM sobrepasa el segundo umbral", "ramusage", bodyText)
        print("RAM sobrepasa el segundo umbral")
        break
    elif dato_RAM >= 85:
        generarGrafica(int(timestampf), int(timestampi))
        send_alert_attached("RAM sobrepasa el tercer umbral", "ramusage", bodyText)
        print("RAM sobrepasa el tercer umbral")
        break

    time.sleep(30)
