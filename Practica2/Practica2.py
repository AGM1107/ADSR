import rrdtool
import glob

# rrdtool.dump('Practica2.rrd', 'Practica2.xml')

data = glob.glob("Practica2_*.png")
print(data.sort())
