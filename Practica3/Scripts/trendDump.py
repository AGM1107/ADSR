import rrdtool

rrdpath = '/home/angelgm/Angel/Servicios en Red/ADSR/Practica3/RRD/'
rrdtool.dump(rrdpath+'monitoreo.rrd', rrdpath+'monitoreo.xml')
