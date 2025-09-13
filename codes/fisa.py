
# import the mudols
from conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def fisaa():
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
        global result1,result2,result3,s,w
        cc = c_ent.get()
        aa = a_ent.get()
        bb = b_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if cc=='' and aa!='' and bb!='':
            result1 = ((int(aa)**2)+(int(bb)**2))**0.5
            w = Label(root, text=f'وتر مثلث: {result1}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=400)
            result2 = f'''
                        🔺 رابطه اصلی:
                            c^2 = a^2 + b^2
                        
                        🔺 از آنجایی که ما c را میخواهیم:
                            c = √(a^2 + b^2)

                        🔺 جایگذاری مقادیر:
                            c = √({aa}^2 + {bb}^2)

                        🔺 سپس:
                            c = √({int(aa)**2} + {int(bb)**2})

                        🔺در نهایت:
                            c = √({(int(aa)**2)+(int(bb)**2)})

                        🔺جواب پایانی:
                            c = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = r2,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
            r2.mainloop()


        elif cc!='' and aa=='' and bb!='':
            result1 = ((int(cc)**2)-(int(bb)**2)) ** 0.5
            w = Label(root, text=f'ضلع غیر وتر اول : {result1}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=400)

            result2 = f'''
                        🔺 رابطه اصلی:
                            c^2 = a^2 + b^2
                            
                        🔺 از آنجا که ما a را میخواهیم:
                            a = √(c^2 - b^2)

                        🔺 جایگذاری مقادیر:
                            a = √({cc}^2 - {bb}^2)

                        🔺 سپس:
                            a = √({int(cc)**2} - {int(bb)**2})

                        🔺در نهایت:
                            a = √({(int(cc)**2)-(int(bb)**2)})

                        🔺جواب پایانی:
                            a = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            
            s=Label(master = r2,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
            r2.mainloop()


        elif cc!='' and aa!='' and bb=='':
            result1 = ((int(cc)**2)-(int(aa)**2))**0.5
            w = Label(root, text=f'ضلع غیر وتر دوم : {result1}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=400)

            result2 = f'''
                        🔺 رابطه اصلی:
                            c^2 = a^2 + b^2
                            
                        🔺 از آنجا که ما a را میخواهیم:
                            b = √(c^2 - a^2)

                        🔺 جایگذاری مقادیر:
                            b = √({cc}^2 - {aa}^2)

                        🔺 سپس:
                            b = √({int(cc)**2} - {int(aa)**2})

                        🔺در نهایت:
                            b = √({(int(cc)**2)-(int(aa)**2)})

                        🔺جواب پایانی:
                            b = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = r2,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
            r2.mainloop()
        else:
            messagebox.showerror(message='اطلاعات نادرست یا ناکافی است!!!')




    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=0,y=0)

    c = Label(master = root,text=(convert('طول وتر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    c_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    c_ent.place(x=400,y=80)
    a = Label(master = root,text=(convert(' طول ضلع غیر وتر اول:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    a_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    a_ent.place(x=400,y=160)

    b = Label(master = root,text=(convert('طول ضلع غیر وتر دوم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    b_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    b_ent.place(x=400,y=240)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=320)

    root.mainloop()