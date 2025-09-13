
# import the mudols
from conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def jazrr():
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

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global lbl 
        try:
            lbl.place_forget()
        except:
            pass
        
        
            
        try:
            aa = int(ad_ent.get())
            tt = int(tav_ent.get())
            lbl = Label(root, text=f'جواب:{aa**(1/tt)}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            lbl.place(x=0, y=300)
        except:
            messagebox.showerror(message='اطلاعات ناکافی یا نادرست میباشد!!')
        
        


            







    ad = Label(master = root,text=(convert('عدد:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    ad_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    ad_ent.place(x=400,y=0)
    tav = Label(master = root,text=(convert('فرجه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    tav_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    tav_ent.place(x=400,y=80)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=160)


    root.mainloop()