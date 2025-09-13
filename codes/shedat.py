
# import the mudols
from conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
#root setting
def shedatt():
    def sound_play():
        import pygame
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
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
        global tt,qq,ii,result2 , result,s,w
        qq = q_ent.get()
        ii = I_ent.get()
        tt = t_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if ii=='' and qq!='' and tt!='':
            result = (int(qq))/(int(tt))
            w=Label(master = root,text=(convert(f'جواب :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'I = Q ÷ t => \nI = {qq} ÷ {tt} => \nI = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif ii!='' and qq=='' and tt!='':
            result = (int(tt))*(int(ii))
            w=Label(master = root,text=(convert(f'جواب :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'Q = I x t => \nQ = {ii} x {tt} => \nQ = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif ii!='' and qq!='' and tt=='':
            result = (int(qq))/(int(ii))
            w=Label(master = root,text=(convert(f'جواب :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f't = Q ÷ I => \nt = {qq} ÷ {ii} => \nt = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        else:
            messagebox.showerror(message='اطلاعات نادرست یا ناکافی است!!!')
        


            





    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)
    Label(master = root,text=(('I : ( Q ÷ t )')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=100,y=400)


    I= Label(master = root,text=(convert('شدت جریان الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    I_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    I_ent.place(x=400,y=80)
    q = Label(master = root,text=(convert('بار الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    q_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q_ent.place(x=400,y=160)

    t = Label(master = root,text=(convert('زمان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    t_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    t_ent.place(x=400,y=240)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=400)



    root.mainloop()