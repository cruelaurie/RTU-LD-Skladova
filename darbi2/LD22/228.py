# Autors: Laura SkladovA	
# Studenta apliecibas numurs: 141REB201
# Datums: 04.02.15.
from math import *
import sys
lenkis = raw_input('Ievadi lenki: ')
if ((int(lenkis) > 0) and (int(lenkis) < 90)):
	r = int(lenkis)*pi/180
else:
	print"Nepareizs lenkis"
	sys.exit();
h = 400
b= cos(r)*h
a = sin(r)*h
file = open("228.svg", "w+")
file.write('<svg height="500" width="600" xmlns="http://www.w3.org/2000/svg">')
file.write('<polygon points="20,')
file.write('%2f,' % a)
file.write('%2f,' % b)
file.write('%2f,' % a)
file.write('%2f,' % b)
file.write('20" style="fill:red;stroke:black;stroke-width:1"/>')
file.write('<text x="300" y="40" fill="000000"> Lenkis ir %d gradi un %f radiani</text>' % (int(lenkis),r))
file.write('</svg>')
file.close()
print "Gatavs!"
