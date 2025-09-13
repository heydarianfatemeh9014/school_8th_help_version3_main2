
# import the mudols
from conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def movazenee():
    def sound_play():
        import pygame
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall1.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    def ent_get():
        sound_play()
        global name_lbl, name_lbl2, result_lbl, result_lbl2, show_lbl, show_lbl2
        
        # try:
            # name_lbl.destroy()
            # name_lbl2.destroy()
            # result_lbl.destroy()
            # result_lbl2.destroy()
            # show_lbl.destroy()
            # show_lbl2.destroy()
            
        # except:
        #     pass
        
        
        megdar_va = va_dahande_ent.get()
        megdar_fara = int(faravarde_ent.get())

        
        


            







    va_dahande = Label(master = root,text=(convert('واکنش دهنده:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)

    va_dahande_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    va_dahande_ent.place(x=400,y=0)
    faravarde = Label(master = root,text=(convert('فراورده:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=150)
    faravarde_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    faravarde_ent.place(x=400,y=150)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=550)


    root.mainloop()