import rrdtool

ret = rrdtool.create("Practica2.rrd",
                     "--start", 'N',
                     "--step", '300',
                     "DS:interfacesMulticast:COUNTER:120:U:U",
                     "DS:paquetesInSuccess:COUNTER:120:U:U",
                     "DS:respuestaICMP:COUNTER:120:U:U",
                     "DS:segmentosTCP:COUNTER:120:U:U",
                     "DS:datagramasRecibidos:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300")

if ret:
    print(rrdtool.error())
