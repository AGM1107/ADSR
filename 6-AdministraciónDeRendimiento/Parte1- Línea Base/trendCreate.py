import rrdtool
ret = rrdtool.create("/home/angelgm/Angel/Servicios en Red/ADSR/6-AdministraciónDeRendimiento/RRD/monitoreo.rrd",
                     "--start", 'N',
                     "--step", '300',
                     "DS:CPUload1:GAUGE:300:0:100",
                     "DS:CPUload2:GAUGE:300:0:100",
                     "DS:CPUload3:GAUGE:300:0:100",
                     "DS:CPUload4:GAUGE:300:0:100",
                     "DS:CPUload5:GAUGE:300:0:100",
                     "DS:CPUload6:GAUGE:300:0:100",
                     "DS:CPUload7:GAUGE:300:0:100",
                     "DS:CPUload8:GAUGE:300:0:100",
                     "DS:CPUload9:GAUGE:300:0:100",
                     "DS:CPUload10:GAUGE:300:0:100",
                     "DS:CPUload11:GAUGE:300:0:100",
                     "DS:CPUload12:GAUGE:300:0:100",
                     "DS:CPUload13:GAUGE:300:0:100",
                     "DS:CPUload14:GAUGE:300:0:100",
                     "DS:CPUload15:GAUGE:300:0:100",
                     "DS:CPUload16:GAUGE:300:0:100",
                     "DS:CPUload:GAUGE:300:0:100",
                     "DS:RAMusage:GAUGE:300:0:100",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500",
                     "RRA:AVERAGE:0.5:1:2500")
if ret:
    print(rrdtool.error())
