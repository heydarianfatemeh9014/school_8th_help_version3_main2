# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from .conv import convert
from .col import*
from .ohm import*
from .shedat import*
from .mv import*
from .masraf import *
def elecc():
        
    #root setting
    root = Tk()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('chemastry lesson')
    #backgroun setting

    image = Image.open('imagess\\wall6.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    
    def ohm():
        root.destroy()
        ohmm()
    def mv():
        root.destroy()
        mvv()
    def shedat():
        root.destroy()
        shedatt()
    def masraf():
        root.destroy()
        masraff()
    ohmm = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= ohm , text=convert('قانون اهم'),font=('Segoe Print',20,'bold')).place(x=150,y=220)
    mogavemat_vige = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= mv , text=convert('مقاومت رسانا'),font=('Segoe Print',20,'bold')).place(x=550,y=220)
    shedat_jarian = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= shedat , text=convert('شدت جریان الکتریکی'),font=('Segoe Print',20,'bold')).place(x=150,y=400)
    masraff = Button(root,bg='#EAE88D',activeforeground='#EAE88D',fg='#767547',activebackground='#767547' ,command= masraf , text=convert('انرژی الکتریکی مصرف شده'),font=('Segoe Print',20,'bold')).place(x=450,y=400)


    root.mainloop()