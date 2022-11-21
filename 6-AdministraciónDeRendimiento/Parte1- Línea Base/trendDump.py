import rrdtool

rrdpath = '/home/angelgm/Angel/Servicios en Red/ADSR/6-AdministraciónDeRendimiento/RRD/'
rrdtool.dump(rrdpath+'monitoreo.rrd', rrdpath+'monitoreo.xml')
