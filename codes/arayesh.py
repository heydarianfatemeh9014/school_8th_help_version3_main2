# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from conv import convert

#root setting
def arayeshh():
    def sound_play():
        import pygame
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('chemastry lesson')
    #backgroun setting

    image = Image.open('imagess\\wall2.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def ent_get():
        sound_play()
        global num_list,name_lbl,bohr_lbl
        try:
            name_lbl.destroy()
        except:
            pass

        try:
            bohr_lbl.destroy()
        except:
            pass

        name_atom = at_name_ent.get()
        number_electrom = int(electron_ent.get())
        
        name_lbl = Label(master = root,text=(f'{name_atom}:'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        name_lbl.place(x=20,y=450)
        number2 = number_electrom
        dor = 1
        num_list = []
        while number2>0:
            new_num = (dor**2)*2
            if number2-new_num<0:
                new_num=number2
            number2-= new_num
            
            num_list.append(int(new_num))
            dor+=1
        num_list.append(number2)
        num_list.pop()

        num_unlist = ')'.join(str(x) for x in num_list)

        bohr_lbl =Label(master = root,text=(f'{num_unlist}'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        bohr_lbl.place(x=100,y=450)
        root2 = Tk()
        if (new_num in [1,2,3]):
            f_no_f = convert('فلز')
        elif (new_num in [5,6,7,8]):
            f_no_f = convert('نافلز')
        elif (new_num in [4]):
            f_no_f = convert('خنثی')
        else:
            f_no_f = convert('تعریف نشده')
        
        f_no_f_lbl = Label(master = root2,text=convert((f'فلز یا نافلز بودن عنصر:{convert(f_no_f)}')),font=('Segoe Print',20,'bold'),bg='white',fg='black')
        f_no_f_lbl.pack()
        e_zarfiat = Label(master = root2,text=convert((f'الکترون ظرفیت:{(new_num)}')),font=('Segoe Print',20,'bold'),bg='white',fg='black')
        e_zarfiat.pack()
        if (new_num in [1,2,3]):
            zarf_atom = new_num
        else:
            zarf_atom = 8-new_num
        atom_zarfiat = Label(master = root2,text=convert((f' اتم ظرفیت:{(zarf_atom)}')),font=('Segoe Print',20,'bold'),bg='white',fg='black')
        atom_zarfiat.pack()


        root2.mainloop()



    at_name = Label(master = root,text=(convert('نام اتم را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    at_name_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    at_name_ent.place(x=400,y=0)
    electron = Label(master = root,text=(convert('تعداد الکترون ها را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=150)
    electron_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    electron_ent.place(x=400,y=150)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=250,y=350)



    name_atom = Entry(master= root,)
    root.mainloop()