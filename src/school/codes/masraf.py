
# import the mudols
from .conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
#root setting
def masraff():
        
    root = Tk()
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
        global result2 , result,w,s
        uu = u_ent.get()
        rr = R_ent.get()
        ii = I_ent.get()
        tt = t_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if uu=='' and rr!='' and ii!='' and tt!='':
            result = (int(rr))*(int(ii))*(int(ii))*(int(tt))
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'u = R x I^2 x t => \nu = {rr} x {ii**2} x {tt} => \nu = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif uu!='' and rr=='' and ii!='' and tt!='':
            result = (int(uu))/((int(ii))*(int(ii))*(int(tt)))
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'R = u ÷ ( I^2 x t ) => \nR = {uu} ÷ ( {ii**2} x {tt} ) => \nR = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif uu!='' and rr!='' and ii=='' and tt!='':
            result = ((int(uu))/((int(rr))*(int(tt))))**0.5
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'I = √(u ÷ (R x t)) => \nI = √({uu} ÷ ( {rr} x {tt} )) => \nI = √{result**2} => \nI = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif uu!='' and rr!='' and ii!='' and tt=='':
            result = (int(uu))/((int(ii))*(int(ii))*(int(rr)))
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f't = u ÷ ( I^2 x R ) => \nt = {uu} ÷ ( {ii} x {rr} ) => \nt = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        else:
            messagebox.showerror(message='اطلاعات نادرست یا ناکافی است!!!')


            






    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)

    u = Label(master = root,text=(convert('انرژی الکتریکی مصرف شده:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    u_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    u_ent.place(x=400,y=80)
    R = Label(master = root,text=(convert('مقاومت الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    R_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    R_ent.place(x=400,y=160)

    I = Label(master = root,text=(convert('شدت جریان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    I_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    I_ent.place(x=400,y=240)

    t = Label(master = root,text=(convert('مدت زمان رابطه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    t_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    t_ent.place(x=400,y=320)

    Label(master = root,text=(('u : R x I^2 x t')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=100,y=400)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=400)


    root.mainloop()