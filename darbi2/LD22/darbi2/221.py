#Fails: 221.py
#Autors: Laura Skladova
#Aplieciibas numurs: 141REB201
#Datums: 18.02.2015

Us = 14.1
R2 = 50

solis = input('Ievadi skaitli: ')
diap0 = input('Ievadiet diapazona saakuma veertiibu: ')
diap1 = input('Ievadiet diapazonu beigu veertiibu: ')
for x in range (diap0, diap1+1, solis):
    I1 = Us/(R2+x)
    Ur = Us-I1*x
    print "R1 = %d\t\t izeja.V = %5.2f\t V1.I = %.3f" % (x,Ur,I1)
