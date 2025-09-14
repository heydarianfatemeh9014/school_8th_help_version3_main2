
# import the mudols
from .conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def ohmm():
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
        global vv,rr,ii , result,result2,s,w
        vv = (V_ent.get())
        rr = (R_ent.get())
        ii = (I_ent.get())
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if vv=='' and ii!='' and rr!='':
            result = int(ii)*int(rr)
            w=Label(master = root,text=(convert(f'اختلاف پتانسیل :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'V = I x R => \nV = {int(ii)} x {int(rr)} => \nV = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif rr=='' and ii!='' and vv!='':
            result = int(vv)/int(ii)
            w=Label(master = root,text=(convert(f'مقاومت رسانا :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'R = V ÷ I => \nR = {int(vv)} ÷ {int(ii)} => \nR = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ii=='' and vv!='' and rr!='':
            result = int(vv)/int(rr)
            w=Label(master = root,text=(convert(f'شدت جریان :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'I = V ÷ R => \nI = {int(vv)} ÷ {int(rr)} => \nI = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        else:
            messagebox.showerror(message='اطلاعات کم یا نادرست است!!!')


        
        
        
        


            






    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)

    V = Label(master = root,text=(convert('اختلاف پتانسیل:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black').place(x=0,y=80)
    V_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    V_ent.place(x=400,y=80)

    R = Label(master = root,text=(convert('مقاومت الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black').place(x=0,y=160)
    R_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    R_ent.place(x=400,y=160)

    I = Label(master = root,text=(convert('شدت جریان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black').place(x=0,y=240)
    I_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    I_ent.place(x=400,y=240)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=300)
    Label(master = root,text=(convert('قانون اهم:\nدر دمای ثابت نسبت اختلاف پتانسیل به شدت جریان\n همواره مقدار ثابتی میباشد\n که به آن مقاومت الکتریکی میگوییم')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=300,y=360)



    root.mainloop()