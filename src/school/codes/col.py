
# import the mudols
from .conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def coll():
        
    #root setting
    root = Tk()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall3.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        global result2 , result,result3
        
        try:
            result.destroy()
            result2.destroy()
            
            
        except:
            pass
        qq1 = abs(int(q1_ent.get()))
        qqq1= int(q1_ent.get())
        qq2 = abs(int(q2_ent.get()))
        qqq2 = int(q2_ent.get())
        rr = int(r_ent.get())
        k = 9*(10**9)
        javab =(qq1*qq2*k)/(rr**2)

        a = 0
        b = ''
        for i in str(javab):
            if i == '0':
                a +=1
            else:
                b+= str(i)
        javab = b+'*10^'+str(a)

        result = Label(master = root,text=((f'اندازه نیرو:{javab}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
        result.place(x=0,y=330)
        if (qqq1>0 and qqq2>0) or (qqq1<0 and qqq2<2):
            noe_niro = 'رانشی'
        else:
            noe_niro = 'ربایشی'
        
        result2 = Label(master = root,text=(convert(f'نوع نیرو:{noe_niro}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
        result2.place(x=0,y=380)
        r2 = Tk()
        r2.geometry('900x900')
        r2.config(bg = 'white')

        real_result_3 = f'''
    🔹 ابتدا قدر مطلق هر دو بار را حساب می‌کنیم:
        {qqq1} => {qq1}
        {qqq2} => {qq2}

    🔹 مقادیر:
        q1 = {qqq1}
        q2 = {qqq2}
        r  = {rr}
        k  = 9 × (10 ^ 9)

    🔹 فرمول محاسبه نیرو:
        F = (q1 × q2 × k) ÷ (r ^ 2)

    🔹 جایگذاری اعداد:
        F = ({qq1} × {qq2} × 9 × (10 ^ 9)) ÷ ({rr} ^ 2)

    🔹 نتیجه نهایی:
        {javab}
    '''

        result3 = Label(master = r2,text=(convert(real_result_3)) ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
        result3.pack()
        r2.mainloop()
        
        
        
        
        


            







    q1 = Label(master = root,text=(convert('q1(بار الکتریکی اول):')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    q1_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q1_ent.place(x=400,y=0)
    q2 = Label(master = root,text=(convert('q2(بار الکتریکی دوم):')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    q2_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q2_ent.place(x=400,y=80)

    r = Label(master = root,text=(convert('r(فاصله بین دو بار):')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    r_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    r_ent.place(x=400,y=160)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=220)




    root.mainloop()