# -*- coding : utf -8 -*-
#Fails :262.py
#Autors: Laura Skladova
#Elektriskaas sheemas animacija
import Tkinter as tk
import time
root = tk.Tk ()
w = tk.Canvas (root , width =300 , height =300 , bg="#234")
w.pack ()
def avots (w, apzimejums , h, xy ):
    w.delete (tk.ALL)
    
    # Sprieguma avota grafika :
    w.create_oval (xy [0] -40 , xy [1]+h/2-40, xy [0] -120 , xy [1]+\
    h/2+40 , width ="3", outline ='#0FF')
    w.create_line (xy [0] -80 , xy [1], xy [0] -80 , xy [1]+h ,\
    width ="3", fill="#0FF")
    
    # Horizontaalu vadu grafika:
    w.create_line (xy [0] -80 , xy [1],xy[0], xy [1] , \
    width ="3", fill="#0FF")
    w.create_line (xy [0] -80 , xy [1]+h,xy[0] , xy [1]+h, \
    width ="3",fill="#0FF")
    
    # Sprieguma avota spailju simbolu grafika :
    w.create_text (xy [0] -70 , xy [1]+h/2 -50 , text='+' ,\
    fill="#FFF", font="Courier 20 bold")
    w.create_text (xy [0] -70 , xy [1]+h/2+50 , text='-' ,\
    fill="#FFF", font="Courier 20 bold")

# Sprieguma vektors
def vektors (w, apzimejums , h, xy ):
    vidus = int(h/2) + xy [1]+3
    delta = 7
    w.create_line (xy [0], vidus +delta ,xy [0] , vidus -delta , \
    arrow ="first", tags= apzimejums , width ="3", \
    fill="#FF0", arrowshape =(10 ,20 ,10))

    newxy = w.coords ( apzimejums )
    N = int ((h-delta )/2 - 10)

    for i in range (N):
        time.sleep (1/100.)
        newxy [3] = newxy [3] - 1
        newxy [1] = newxy [1] + 1
        w.coords (apzimejums , * newxy )
        w.update ()
        
    w.create_text (xy [0] + 20, xy [1] + h/2, text='U1 ', \
    fill="#FFF", font=" Courier 20")

def fun ():
    avots (w, "V1", 200, [150 , 50])

def fun2 ():
    vektors (w, "U1", 200 , [150 , 50])


def fun3 ():
    w.delete('U1')
    

b = tk.Button (root , text="Shema", command =fun)
b.pack(side="left")

b2 = tk.Button (root , text=" Spriegums ", command =fun2)
b2.pack(side="left")

b3 = tk.Button (root , text=" Noņem spriegumu ", command =fun3)
b3.pack(side="top")

root.mainloop ()

