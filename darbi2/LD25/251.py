#Fails 251.py
#Laura Skladova
import Tkinter as tk

root=tk.Tk()
root.title("Mana bilde")
w=tk.Canvas(root,width=600,height=400, bg="#abc")
w.pack()
linija=w.create_line(50, 100, 400, 300)

root.mainloop()
