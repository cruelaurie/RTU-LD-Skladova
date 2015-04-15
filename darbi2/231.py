# Fails 231. py
# Autors Laura Skladova

from PythonMagick import Image
bilde = Image ( "3x3", "#22aaff" )
x = y = 0
bilde . pixelColor ( x, y, "#eeff22 " )
bilde . scale ( "200x200" )
bilde . write ( "231.png" )
