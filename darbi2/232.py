# Fails 232. py
# Autors Laura Skladova
from PythonMagick import Image
bilde = Image ( "16x16", "#28aaff" )
x = y = 0
bilde . pixelColor (0,0, "#eeff28" )
bilde . pixelColor (0,1, "#eeff28" )
bilde . pixelColor (0,2, "#eeff28" )
bilde . pixelColor (0,3, "#eeff28" )
bilde . pixelColor (1,3, "#eeff28" )
bilde . pixelColor (2,3, "#eeff28" )
bilde . write ( "232.png" )
bilde.scale ("200x200")
