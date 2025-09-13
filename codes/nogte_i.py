
# import the mudols
from conv import convert
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from tkinter import messagebox
def nogte_ii():
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

    image = Image.open('imagess\\yellow.jpg')
    image = image.resize((800,800))

    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def ent_get():
        sound_play()
        global name_lbl, name_lbl2, result_lbl, result_lbl2, show_lbl, show_lbl2
        
        try:
            name_lbl.destroy()
            name_lbl2.destroy()
            result_lbl.destroy()
            result_lbl2.destroy()
            show_lbl.destroy()
            show_lbl2.destroy()
            
        except:
            pass
        
        
        name_atom = at_name_ent.get()
        number_electrom = int(electron_ent.get())
        name_atom2 = at_name_ent2.get()
        number_electrom2 = int(electron_ent2.get())
        
        

        num_num1 = number_electrom
        num_num2 = number_electrom2
        n1 = 1
        n2 = 1
        y = False


        if number_electrom in [1,2,3]: num1 = True 
        else: num1 = False


        if number_electrom2 in [1,2,3]:num2 = True
        else:num2 = False

        if num1==True and num2==True:
            y=True
            messagebox.showerror(message=(('هر دو فلز نمیشود! یک فلز و یک نافلز')))
        if num1==False and num2==False:
            y = True
            messagebox.showerror(message=(('هردو نافلز نمیشود! یک فلز و یک نافلز')))
        if number_electrom == 4 or number_electrom2==4:
            y = True
            messagebox.showinfo(message=(('خنثی ترکیب نمیسازد!')))
        if number_electrom>8 or number_electrom2>8:
            y = True
            messagebox.showinfo(message=(('درست نیست.بیشتر از 8 نمیتونه باشه')))
        if number_electrom==8 or number_electrom2==8:
            y = True
            messagebox.showinfo(message=(('یکیشون پایداره نمیخواد بگیره.')))

        


        
        # تا زمانی که وای ترو نیست اگر اولی ترو(فلز) و دومی فالس(نافلز) باشد تا زمانی که  اولی صفر و دومی هشت(پایدار نشده باشه ادامه داره
        #خوب از فلز کم میشه میره به نافلز اما اگر اولی پایدار و دومی نشده بود قدار اولی رو دووباره برابر اولش میکنیم انگار یک عنصر جدید اضافه کردیم
        #و نام یک +1 میشه چون تعداد رو نشون میده.اگر اولی صفر نشده دومی هشت هم به همین صورت و اگر اولی صفر دومی هشت وای برابر ترو و حلقه تمام
        if y==False:
            while y==False:
                if num1==True and num2 ==False:
                    while num_num1>0 and num_num2<8:
                        num_num1-=1
                        num_num2+=1
                        if num_num1==0 and num_num2!=8:
                            num_num1 = number_electrom
                            n1+=1
                        if num_num1!=0 and num_num2==8:
                            num_num2= number_electrom2
                            n2+=1
                        if num_num1==0 and num_num2==8:
                            y=True

                if num2==True and num1 ==False:
                    while num_num2>0 and num_num1<8:
                        num_num2-=1
                        num_num1+=1
                        if num_num2==0 and num_num1!=8:
                            num_num2 = number_electrom2
                            n2+=1
                        if num_num2!=0 and num_num1==8:
                            num_num1= number_electrom
                            n1+=1
                        if num_num2==0 and num_num1==8:
                            y=True
        name_lbl = Label(master = root,text=(f'{name_atom}:'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        name_lbl.place(x=200,y=550)
        num_el_2 = number_electrom-(number_electrom//2)
        num_el_3 = number_electrom//2
        dots = '.' * num_el_3
        dots2 = '.' * num_el_2
        result = dots + name_atom + dots2+'   '
        result_lbl = Label(master = root,text=(n1*result),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        result_lbl.place(x=200,y=550)

        name_lbl2 = Label(master = root,text=(f'{name_atom2}:'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        name_lbl2.place(x=200,y=650)
        num_el_22 = number_electrom2-(number_electrom2//2)
        num_el_32 = number_electrom2//2
        dots2 = '.' * num_el_32
        dots22 = '.' * num_el_22
        result2 = dots2 + name_atom2 + dots22+'   '
        result_lbl2 = Label(master = root,text=(n2*result2),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        result_lbl2.place(x=200,y=650)

        show_lbl = Label(master = root,text=(convert(f' {name_atom} : {n1}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
        show_lbl.place(x=0,y=650)
        show_lbl2 = Label(master = root,text=(convert(f' {name_atom2} : {n2}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
        show_lbl2.place(x=0,y=750)
        a=3
        


            







    at_name = Label(master = root,text=(convert('نام اتم اول را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)

    at_name_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    at_name_ent.place(x=400,y=0)
    electron = Label(master = root,text=(convert(' تعداد الکترون های آخرین لایه اتم اول:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=150)
    electron_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    electron_ent.place(x=400,y=150)

    at_name2 = Label(master = root,text=(convert('نام اتم دوم را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=300)
    at_name_ent2 = Entry(master=root,font=('Segoe Print',20,'bold'))
    at_name_ent2.place(x=400,y=300)
    electron2 = Label(master = root,text=(convert(' تعداد الکترون های آخرین لایه اتم دوم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=450)
    electron_ent2 = Entry(master=root,font=('Segoe Print',20,'bold'))
    electron_ent2.place(x=400,y=450)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=550)



    root.mainloop()