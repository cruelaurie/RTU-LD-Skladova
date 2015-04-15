# Fails 233. py
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

bilde . pixelColor (5,0, "#eeff28" )
bilde . pixelColor (6,0, "#eeff28" )
bilde . pixelColor (7,0, "#eeff28" )
bilde . pixelColor (8,0, "#eeff28" )
bilde . pixelColor (4,1, "#eeff28" )
bilde . pixelColor (4,2, "#eeff28" )
bilde . pixelColor (5,3, "#eeff28" )
bilde . pixelColor (6,3, "#eeff28" )
bilde . pixelColor (7,3, "#eeff28" )
bilde . pixelColor (8,3, "#eeff28" )
bilde . pixelColor (8,4, "#eeff28" )
bilde . pixelColor (5,5, "#eeff28" )
bilde . pixelColor (6,5, "#eeff28" )
bilde . pixelColor (7,5, "#eeff28" )
bilde . pixelColor (8,5, "#eeff28" )
bilde . write ( "233.png" )
bilde.scale ("200x200")
