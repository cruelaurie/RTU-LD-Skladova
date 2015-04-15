#Autors: Laura Skladova
#Uzdevums 243.py

from Tkinter import *
import time



w=Tk()
uzrA=Label(w,bg="#F5D0A9", text='Laura Skladova, 141REB201, REBC04')
uzrAB=Label(w,bg="#F5D0A9", text='Rigas tehniska universitate, Elektronikas un Telekomunikaciju fakultate')
uzrABC=Label(w,bg="#F5D0A9", text='2015. gads')
uzrA.place(x=400, y=100)
uzrAB.place(x=300, y=120)
uzrABC.place(x=470, y=140)

uzr00=Label(w,bg="#DF0101", text='Pirmdiena')
uzr01=Label(w,bg="#FE2E2E", text='1. 8:15 - 9:50 Elektorinikas Teoretiskie Pamati, Lab.d')
uzr02=Label(w,bg="#FA5858", text='2. 10:15 - 11:50 Elektronikas Teorētiskie Pamati, Pr.d')
uzr03=Label(w,bg="#F78181", text='3. 12:30 - 14:05 Sports')
uzr04=Label(w,bg="#F5A9A9", text='4. 14:05 - 16:05 Elektroinzenieru matematikas datorrealizacija, Lab.d')
uzr00.place(x=50, y=180)
uzr01.place(x=10, y=200)
uzr02.place(x=10, y=220)
uzr03.place(x=10, y=240)
uzr04.place(x=10, y=260)

uzr00=Label(w,bg="#0000FF", text='Otrdiena')
uzr01=Label(w,bg="#5858FA", text='1. 8:15 - 9:50 Matematika, Pr.d')
uzr02=Label(w,bg="#8181F7", text='2. 10:15 - 11:50 Matematika, Lekc')
uzr03=Label(w,bg="#A9A9F5", text='3. 12:30 - 14:05 Elektronikas Teoretiskie Pamati, Lekc.')
uzr00.place(x=550, y=180)
uzr01.place(x=500, y=200)
uzr02.place(x=500, y=220)
uzr03.place(x=500, y=240)

uzr00=Label(w,bg="#DF3A01", text='Tresdiena')
uzr01=Label(w,bg="#FE642E", text='1. 8:15 - 9:50 Datormācība, Lekc')
uzr02=Label(w,bg="#FA8258", text='2. 10:15 - 11:50 Elektronikas Teorētiskie Pamati, Lekc.')
uzr03=Label(w,bg="#F79F81", text='3. 12:30 - 14:05 Fizika, Lekc.')
uzr04=Label(w,bg="#F5BCA9", text='4. 14:05 - 16:05 Datormācība, Pr.d')
uzr00.place(x=50, y=300)
uzr01.place(x=10, y=320)
uzr02.place(x=10, y=340)
uzr03.place(x=10, y=360)
uzr04.place(x=10, y=380)

uzr00=Label(w,bg="#01DF01", text='Ceturtdiena')
uzr01=Label(w,bg="#2EFE2E", text='1. 8:15 - 9:50 Elektroinzenieru matematikas datorrealizacija, Lekc')
uzr02=Label(w,bg="#58FA58", text='2. 10:15 - 11:50 Elektriba un magnetisms, Lekc')
uzr03=Label(w,bg="#81F781", text='3. 12:30 - 14:05 Sports')
uzr00.place(x=550, y=300)
uzr01.place(x=500, y=320)
uzr02.place(x=500, y=340)
uzr03.place(x=500, y=360)

uzr00=Label(w,bg="#D7DF01", text='Piektdiena')
uzr01=Label(w,bg="#F7FE2E", text='1. 8:15 - 9:50 Anglu val.')
uzr02=Label(w,bg="#F4FA58", text='2. 10:15 - 11:50 Para ned. Matematika, Pr.d / Nepara ned. Fizika, Lab.d')
uzr03=Label(w,bg="#F3F781", text='3. 12:30 - 14:05 Ned. 5, 7, 9, 11, Elektriba un magnetisms, Lab.d')
uzr00.place(x=50, y=420)
uzr01.place(x=10, y=440)
uzr02.place(x=10, y=460)
uzr03.place(x=10, y=480)

w.geometry('1000x800')
w.title('Stundu saraksts')

def mirgot():
    t = time.localtime(time.time())
    if t[5] % 2:                                
        fmt="%H:%M:%S"
    else:
        fmt="%H %M %S"
    time_var.set(time.strftime(fmt, t))
    time_labelis.after(500, mirgot)         
    
w=Tk(); f=Frame(); f.pack()
time_var=StringVar()
time_labelis=Label(f, textvariable=time_var, font="Courier 60", bg="White", fg="#000000")
time_labelis.pack()

time_labelis.after(500, mirgot)

w.mainloop()
