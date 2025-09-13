# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from conv import convert
from tavan import*
from jazr import*
from fisa import*
#root setting
def riazii():
    def sound_play():
        import pygame
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('Math lesson')
    #backgroun setting

    image = Image.open('imagess\\yellow.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)


    def tavv():
        
        sound_play()
        tavann()

    def jazr():

        sound_play()
        jazrr()

    def fisa():

        sound_play()
        fisaa()
    # moadele = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= chimi , text=convert('معادله'),font=('Segoe Print',20,'bold')).place(x=250,y=20)
    tavan = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= tavv , text=convert('توان  '),font=('Segoe Print',20,'bold')).place(x=250,y=20)
    jazzr = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= jazr , text=convert('جذر'),font=('Segoe Print',20,'bold')).place(x=250,y=170)
    fisagores = Button(root,bg='#A4EBD6',activeforeground='#A4EBD6',fg='#3E5850',activebackground='#3E5850' ,command= fisa , text=convert('فیثاغورس'),font=('Segoe Print',20,'bold')).place(x=250,y=320)
    # dayere = Button(root,bg='#EAE88D',activeforeground='#EAE88D',fg='#767547',activebackground='#767547' ,command= chimi , text=convert('دایره ها'),font=('Segoe Print',20,'bold')).place(x=250,y=470)


    root.mainloop()