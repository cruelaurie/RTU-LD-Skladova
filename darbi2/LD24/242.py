#Laura Skladova
#242.py
from Tkinter import *
import time

w = Tk(); f = Frame(); f.pack()
time_var = StringVar()
time_labelis = Label(f, textvariable=time_var,
font="Courier 60",
bg="Black", fg="#00B000")
time_labelis.pack()

def mirgot():
    """Funkciju datu atjaunosanai"""
    t = time.localtime(time.time())
    print t
    if t[6] % 2:
        fmt = "%H:%M:%S"
    else:
        fmt = "%H %M %S"
        time_var.set(time.strftime(fmt, t))
        time_labelis.after(1, mirgot)

time_labelis.after(1, mirgot)
w.mainloop()
