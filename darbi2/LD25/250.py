#-*- coding: utf -8 -*-
# Fails : 250.py
# Autors: Laura Skladova
import Tkinter as tk
root= tk.Tk();
root.title("Mana Tafele")

v=tk.StringVar()
v.set('Teksts uz tafeles')

def fun():
    
    e=tk.Entry(root, textvariable=v)
    e.pack()
    w.itemconfig(t, text=e.get())

b=tk.Button(root, text="Spied", command=fun)
b.pack()

v=tk.StringVar
w = tk.Canvas(root, width=600, height=400,bg="#e5e5b7", relief="sunken", border=10)

t = w.create_text(50, 100, anchor='nw', text="2+2=4",font="Courier 40 italic", fill ="#000000")

t = w.create_text(500, 100, anchor='n', text="Laura Skladova",font="Courier 20 italic", fill ="#000000")
             

w.pack()
w.mainloop()

