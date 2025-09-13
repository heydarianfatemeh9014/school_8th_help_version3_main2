
# import the mudols
from conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
#root setting
def motegatee():
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

    image = Image.open('imagess\\wall8.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global s,w , javab,result2
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        aa = α_ent.get()
        nn = N_ent.get()
        if aa=='' and nn!='':
            javab = 360/(int(nn)+1)
            w=Label(master = root,text=((f'اندازه α:{javab}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'α = 360 ÷ (n+1) => \nα = 360 ÷ ( {nn} + 1 ) => \nα = 360 ÷ ( {int(nn)+1} ) => \nα = {javab}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
        elif aa!='' and nn=='':
            javab = (360/(int(aa)))-1
            w=Label(master = root,text=((f'اندازه n:{javab}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'n = ( 360 ÷ α ) - 1 => \nn = ( 360 ÷ {aa} ) - 1 => \nn = ( {360 / int(aa)} ) + 1 => \nn = {javab}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
        else:
            messagebox.showerror(message='اطلاعات ناکافی یا نادرست است!')
        
        
        


            






    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)

    N = Label(master = root,text=(convert('تعداد تصاویر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    N_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    N_ent.place(x=400,y=80)
    α = Label(master = root,text=(convert('زاویه بین دو آینه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    α_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    α_ent.place(x=400,y=160)

    Label(master = root,text=(convert('n = (360 ÷ α ) - 1')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=150,y=300)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=300)


    root.mainloop()