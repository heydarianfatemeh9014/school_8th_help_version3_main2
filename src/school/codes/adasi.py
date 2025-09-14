
# import the mudols
from .conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
#root setting
def adasii():
    root = Tk()
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
        global w,s,result,result1,result3 , result2
        qq = q_ent.get()
        pp = p_ent.get()
        aabb = ab_ent.get()
        aabbb = abb_ent.get()
        ff = f_ent.get()
        rr = r_ent.get()
        mm = m_ent.get()
        dd = d_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass

        if qq == '?' and pp != '' and (ff != '' or rr != ''):
            if ff != '':
                result1 = (1 / int(ff)) - (1 / int(pp))
                result2 = f'''
                    🔺 رابطه اصلی:
                        (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                    🔺 چون q را می‌خواهیم:
                        (1 ÷ q) = (1 ÷ f) - (1 ÷ p)

                    🔺 جایگذاری مقادیر:
                        (1 ÷ q) = (1 ÷ {int(ff)}) - (1 ÷ {int(pp)})

                    🔺 ساده‌سازی:
                        (1 ÷ q) = {1/int(ff)} - {1/int(pp)}

                    🔺 مقدار عددی:
                        (1 ÷ q) = {result1}

                    🔺 در نهایت:
                        q = {1 / result1}
                    '''

            else:
                ff = int(rr) / 2

                result1 = (1 / int(ff)) - (1 / int(pp))
                result2 = f'''
                            🔺 رابطه اصلی:
                                (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                            🔺 از آنجایی که ما f را نداریم:
                                f = r ÷ 2
                                r = {rr} 
                                f = {rr} ÷ 2 
                                f = {int(rr)/2}
                                                
                            🔺 چون q را می‌خواهیم:
                                (1 ÷ q) = (1 ÷ f) - (1 ÷ p)

                            🔺 جایگذاری مقادیر:
                                (1 ÷ q) = (1 ÷ {int(ff)}) - (1 ÷ {int(pp)})

                            🔺 ساده‌سازی:
                                (1 ÷ q) = {1/int(ff)} - {1/int(pp)}

                            🔺 مقدار عددی:
                                (1 ÷ q) = {result1}

                            🔺 در نهایت:
                                q = {1 / result1}
                            '''

            result = 1 / result1
            w=Label(root, text=f'فاصله تصویر تا عدسی: {result:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)

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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp == '?' and (ff != '' or rr != ''):
            if ff != '':
                result1 = (1 / int(ff)) - (1 / int(qq))

                result2 = f'''
                    🔺 رابطه اصلی:
                        (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                    🔺 چون p را می‌خواهیم:
                        (1 ÷ p) = (1 ÷ f) - (1 ÷ q)

                    🔺 جایگذاری مقادیر:
                        (1 ÷ p) = (1 ÷ {int(ff)}) - (1 ÷ {int(qq)})

                    🔺 ساده‌سازی:
                        (1 ÷ p) = {1/int(ff)} - {1/int(qq)}

                    🔺 مقدار عددی:
                        (1 ÷ p) = {result1}

                    🔺 در نهایت:
                        p = {1 / result1}
                    '''


            else:
                ff = int(rr) / 2
                result1 = (1 / int(ff)) - (1 / int(qq))

                result2 = f'''
                            🔺 رابطه اصلی:
                                (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                            🔺 از آنجایی که ما f را نداریم:
                                f = r ÷ 2
                                r = {rr} 
                                f = {rr} ÷ 2 
                                f = {int(rr)/2}
                                                
                            🔺 چون p را می‌خواهیم:
                                (1 ÷ p) = (1 ÷ f) - (1 ÷ q)

                            🔺 جایگذاری مقادیر:
                                (1 ÷ p) = (1 ÷ {int(ff)}) - (1 ÷ {int(qq)})

                            🔺 ساده‌سازی:
                                (1 ÷ p) = {1/int(ff)} - {1/int(qq)}

                            🔺 مقدار عددی:
                                (1 ÷ p) = {result1}

                            🔺 در نهایت:
                                p = {1 / result1}
                            '''
            result = 1 / result1
            w=Label(root, text=f'فاصله جسم تا عدسی: {result:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp != '' and aabb == '?' and aabbb != '':
            result1 = (int(aabbb) * abs(int(pp))) / abs(int(qq))
            result2 = f'''
                        🔺 رابطه اصلی:
                            ( 'p| ÷ |q| ) = ( ab ÷ a'b| )

                        🔺 از آنجایی که ما ab را نداریم:
                            |ab = ( a'b' x |p| ) ÷ |q

                        🔺 جایگذاری مقادیر:
                            ab = ( {aabbb} x {abs(int(pp))} ) ÷ {abs(int(qq))}

                        🔺 ساده‌سازی:
                            ab = ({int(aabbb)*(abs(int(pp)))}) ÷ {abs(int(qq))}

                        🔺 در نهایت:
                            ab = {result1}
                        '''
            w=Label(root, text=f'طول جسم: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp != '' and aabb != '' and aabbb == '?':
            result1 = (int(aabb) * abs(int(qq))) / abs(int(pp))
            result2 = f'''
                        🔺 رابطه اصلی:
                            ( 'p| ÷ |q| ) = ( ab ÷ a'b| )

                        🔺 از آنجایی که ما a'b' را نداریم:
                            |a'b' = ( ab x |q| ) ÷ |p

                        🔺 جایگذاری مقادیر:
                            a'b' = ( {aabb} x {abs(int(qq))} ) ÷ {abs(int(pp))}

                        🔺 ساده‌سازی:
                            a'b' = ({int(aabb)*(abs(int(qq)))}) ÷ {abs(int(pp))}

                        🔺 در نهایت:
                            ab = {result1}
                        '''


            w=Label(root, text=f'طول تصویر: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or rr != '' or dd!='') and ff == '?':
            if rr != '':
                result1 = int(rr) / 2
                result2 = f'''
                        🔺 رابطه اصلی:
                            R = 2f

                        🔺 از آنجایی که ما f را نداریم:
                            f = R ÷ 2

                        🔺 جایگذاری مقادیر:
                            f = {rr} ÷ 2

                        🔺 در نهایت:
                            f = {result1}
                        '''
            elif dd!='':
                result1 = 1/int(dd)

                result2 = f'''
                        🔺 رابطه اصلی:
                            f = 1 ÷ d

                        🔺 جایگذاری مقادیر:
                            f = 1 ÷ {dd}

                        🔺 در نهایت:
                            f = {result1}
                        '''
            
            else:
                result1 = 1 / ((1 / int(qq)) + (1 / int(pp)))

                result2 = f'''
                        🔺 رابطه اصلی:
                            1 ÷ f = ( 1 ÷ p ) + ( 1 ÷ q )

                        🔺 جایگذاری مقادیر:
                            1 ÷ f = ( 1 ÷ {pp} ) + ( 1 ÷ {qq} )

                        🔺 ساده‌سازی:
                            1 ÷ f = ( {1/(int(pp))} ) + ( {1/(int(qq))} )

                        🔺 پس از آن:
                            1 ÷ f =  {(1/(int(pp))) + (1/(int(qq)))}

                        🔺 در نهایت:
                            f = {result1}
                        '''
            


            w=Label(root, text=f'فاصله کانونی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or ff != '') and rr == '?':
            if qq != '' and pp != '':
                result1 = (1 / ((1 / float(qq)) + (1 / float(pp)))) * 2
            else:
                result1 = int(ff) * 2
            w=Label(root, text=f'شعاع: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or (aabb != '' and aabbb != '')) and mm == '?':
            if qq != '' and pp != '':
                result1 = abs(int(qq)) / abs(int(pp))
            else:
                result1 = int(aabbb) / int(aabb)
            w=Label(root, text=f'بزرگ نمایی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)

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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
        elif dd=='?' and ff!='':
            result1 = 1/int(ff)
            result2 = f'''
                        🔺 رابطه اصلی:
                            d = 1 ÷ f

                        🔺 جایگذاری مقادیر:
                            d = 1 ÷ {ff}

                        🔺 در نهایت:
                            d = {result1}
                        '''
            
            w=Label(root, text=f'توان عدسی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
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
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        else:
            messagebox.showwarning('هشدار', 'لطفاً مقدار درست وارد کن! حالت نامعتبره 😢')

        




    Label(master = root,text=(convert(' مقدار هر یک را که مربوط به مسئله است را وارد کنید و مقادیر خواسته شده را ? بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=0,y=0)


    ab = Label(master = root,text=(convert('طول جسم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    ab_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    ab_ent.place(x=400,y=80)
    abb = Label(master = root,text=(convert('طول تصویر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    abb_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    abb_ent.place(x=400,y=160)

    p = Label(master = root,text=(convert('فاطله جسم تا عدسی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    p_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    p_ent.place(x=400,y=240)


    q = Label(master = root,text=(convert('فاطله تصویر تا عدسی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    q_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q_ent.place(x=400,y=320)


    r = Label(master = root,text=(convert('شعاع:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=400)
    r_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    r_ent.place(x=400,y=400)

    f = Label(master = root,text=(convert('فاصله کانونی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=480)
    f_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    f_ent.place(x=400,y=480)

    m= Label(master = root,text=(convert('بزرگ نمایی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=560)
    m_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    m_ent.place(x=400,y=560)
    d= Label(master = root,text=(convert('توان عدسی')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=640)
    d_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    d_ent.place(x=400,y=640)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=300,y=700)


    root.mainloop()