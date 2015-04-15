# -*- coding : utf -8 -*-
#Fails :260.py
#Autors:Laura Skladova
#Veidojam Tafeli ar uzrakstu : 0123456789 ABCDEF
#Programma uz tafeles tekstu raksta nesteidzoties :pa vienam burtam pussekundee

import Tkinter as tk
import time
root= tk.Tk ()
root. title ("Mana Tafele ar dinamisku tekstu")

w = tk. Canvas (root , width =600 , height =400 ,bg="#456", relief ="sunken", border =10 )
w.pack()

t = w. create_text (50 , 100 , text="2 + 2 = \n4" ,font="Courier 40 bold", fill ="#ffc", anchor ="nw")

def funA ():
    k = 16
    s = e2.get()
    for i in range (k):
        print s[:i]
        w.itemconfig (t, text=s[:i])
        w.update()
        time.sleep(0.1)
def funB():
    k = 16
    s = e2.get()
    for i in range (k+2):
        w.itemconfig(t, text=s[i:])
        w.update()
        time.sleep(0.1)

        
        
v = tk. StringVar()
v.set("0123456789 ABCDEF")

e2 = tk. Entry (root , textvariable =v)
e2.pack ()

b = tk. Button (root , text="Spied", command =funA)
b.pack ()
b2=tk. Button (root , text="Spied", command =funB)
b2.pack ()
root. mainloop ()

