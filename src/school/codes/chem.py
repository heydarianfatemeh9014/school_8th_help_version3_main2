# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from .conv import convert
from .atom import *
from .nogte_i import *
from .movazene import*
from .arayesh import*
def chemm():
        
    #root setting
    root = Tk()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('chemastry lesson')
    #backgroun setting

    image = Image.open('imagess\\wall2.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def atom():
        root.destroy()
        
        atomm()
    def arayesh():
        root.destroy()
        arayeshh()
   
    def nogte_i():
        root.destroy()
        nogte_ii()
    

    atom = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= atom , text=convert('ریز ترین ذرات تشکیل دهنده مواد'),font=('Segoe Print',20,'bold')).place(x=250,y=20)
    arayesh = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= arayesh , text=convert('  آرایش الکترونی به روش بور  '),font=('Segoe Print',20,'bold')).place(x=250,y=170)
    electro_dot = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= nogte_i , text=convert('  مدل الکترو نقطه ای اتم ها    '),font=('Segoe Print',20,'bold')).place(x=250,y=320)
    # vaconesh = Button(root,bg='#A4EBD6',activeforeground='#A4EBD6',fg='#3E5850',activebackground='#3E5850' ,command= movazene , text=convert('       موازنه ی واکنش ها     '),font=('Segoe Print',20,'bold')).place(x=250,y=470)

    def back():  # تعریف تابع برای بازگشت به صفحه اصلی
        run(['python', 'main.py'])  # اجرای فایل خارجی main.py

    # ایجاد دکمه‌ها با تنظیمات مختلف
    back_bt = Button(root, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=250, y=650)

    root.mainloop()