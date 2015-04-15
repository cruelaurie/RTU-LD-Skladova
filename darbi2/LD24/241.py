#Autors :Laura Skladova
#241.py

from Tkinter import *
w=Tk()
uzr001=Label(w,bg="#28c", text='Laura Skladova, 141REB201, REBC04')
uzr0001=Label(w,bg="#28c", text='Rigas tehniska universitate, Elektronikas un Telekomunikaciju fakultate')
uzr00001=Label(w,bg="#28c", text='2015. gads')
uzr01=Label(w,bg="#28c", text='1. Datormācība, Lekc')
uzr02=Label(w,bg="#38c", text='2. Elektronikas Teorētiskie Pamati')
uzr03=Label(w,bg="#48c", text='3. Fizikaa')
uzr04=Label(w,bg="#58c", text='4. Datormaciba, Pr.d')
uzr001.place(x=300, y=10)
uzr0001.place(x=200, y=30)
uzr00001.place(x=370, y=50)
uzr01.place(x=270, y=80)
uzr02.place(x=270, y=100)
uzr03.place(x=270, y=120)
uzr04.place(x=270, y=140)
w.geometry('800x600')
w.title('Stundu saraksts 18.02.2015')
w.mainloop()
