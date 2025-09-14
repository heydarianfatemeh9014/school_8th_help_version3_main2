
# import the mudols
from .conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def mvv():
        
    #root setting
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
        global vv,rr,ii , result,result2,w,s
        pp = P_ent.get()
        ll = L_ent.get()
        aa = A_ent.get()
        rr = R_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        
        if rr=='' and ll!='' and aa!='' and pp!='':
            result = ((int(pp))*(int(ll)))/(int(aa))
            w=Label(master = root,text=(convert(f'.جواب حاصل مقاومت رسانا:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'R = ( ρ x L ) ÷ A => \nR = ( {int(pp)} x {int(ll)} ) ÷ {int(aa)} => \nR = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif rr!='' and ll!='' and aa!='' and pp=='':
            result = ((int(aa))*(int(rr)))/(int(ll))
            w=Label(master = root,text=(convert(f'جواب حاصل :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'ρ = ( A x R ) ÷ L => \nρ = ( {int(aa)} x {int(rr)} ) ÷ {int(ll)} => \nρ = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif rr!='' and ll=='' and aa!='' and pp!='':
            result = ((int(aa))*(int(rr)))/(int(pp))
            w=Label(master = root,text=(convert(f'جواب حاصل :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'L = ( A x R ) ÷ ρ => \nL = ( {int(aa)} x {int(rr)} ) ÷ {int(pp)} => \nL = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif rr!='' and ll!='' and aa=='' and pp!='':
            result = ((int(pp))*(int(ll)))/(int(rr))
            w=Label(master = root,text=(convert(f'جواب حاصل سطح مقطع:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'A = ( P x L ) ÷ R => \nA = ( {int(pp)} x {int(ll)} ) ÷ {int(rr)} => \nA = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        else:
            messagebox.showerror(message = 'اطلاعات کم یا نادرست است!!')
        
        
        
        


            





    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)


    P= Label(master = root,text=(convert('مقاومت ویژه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    P_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    P_ent.place(x=400,y=80)
    L_l = Label(master = root,text=(convert('طول رسانا:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    L_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    L_ent.place(x=400,y=160)

    A_a = Label(master = root,text=(convert('سطح مقطع:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    A_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    A_ent.place(x=400,y=240)

    R_r = Label(master = root,text=(convert('مقاومت رسانا:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    R_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    R_ent.place(x=400,y=320)

    Label(master = root,text=(('R : ( L x ρ ) ÷ A')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=100,y=400)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=400)



    root.mainloop()