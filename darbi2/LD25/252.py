#252.py
#Laura Skladova

import Tkinter as tk

root=tk.Tk()
root.title("Televīzijas krāsu tabula")
w=tk.Canvas (root,width=800,height=450,bg="#abc")
w.pack()
linija1=w.create_line(50,0,50,800,width=100, fill="#FFFFFF")
linija2=w.create_line(150,0,150,800,width=100,fill="#FFFF00")
linija3=w.create_line(250,0,250,800,width=100, fill="#00FFFF")
linija4=w.create_line(350,0,350,800,width=100, fill="#00FF00")
linija5=w.create_line(450,0,450,800, width=100,fill="#9900cc")
linija6=w.create_line(550,0,550,800, width=100, fill="#FF0000")
linija7=w.create_line(650,0,650,800,width=100, fill="#0000FF")
linija8=w.create_line(750,0,750,800,width=100,fill="#000000")
root.mainloop()
