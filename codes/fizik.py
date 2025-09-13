# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from conv import convert
from adasi import*
from col import*
from elec import*
from aine import*
from motegate import*
def fizikk():
    def sound_play():
        import pygame
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('lesson')
    #backgroun setting

    image = Image.open('imagess\\wall4.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def adasi():

        sound_play()
        adasii()

    def cool():

        sound_play()
        coll()

    def eleec():

        sound_play()
        elecc()

    def motegatte():

        sound_play()
        motegatee()

    def aiine():

        sound_play()
        ainee()
    colon = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= cool , text=convert('مسائل کولن'),font=('Segoe Print',20,'bold')).place(x=150,y=220)
    elecctric = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= eleec , text=convert('جریان الکتریکی'),font=('Segoe Print',20,'bold')).place(x=550,y=220)
    moteggate = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= motegatte , text=convert('آینه های متقاطع'),font=('Segoe Print',20,'bold')).place(x=150,y=400)
    ainne = Button(root,bg='#A4EBD6',activeforeground='#A4EBD6',fg='#3E5850',activebackground='#3E5850' ,command= aiine , text=convert('آینه ها'),font=('Segoe Print',20,'bold')).place(x=550,y=400)
    adasiii = Button(root,bg='#EAE88D',activeforeground='#EAE88D',fg='#767547',activebackground='#767547' ,command= adasi , text=convert('عدسی ها'),font=('Segoe Print',20,'bold')).place(x=350,y=580)


    root.mainloop()