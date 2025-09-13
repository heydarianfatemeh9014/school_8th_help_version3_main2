# import the modules
from tkinter import *
from PIL import Image, ImageTk
def atomm():
    def sound_play():
        import pygame
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    global icon_label,backgr,icon_image_original,angle
        
    # root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False, False)
    root.title('Chemistry Lesson')

    icon_image_original = Image.open('imagess\\atom.png').resize((300, 300))  # اندازه‌ش کوچیکه
    icon_photo = None  # عکس چرخیده‌ش
    icon_label = None  # لیبل اون عکس
    angle = 0  # زاویه برای چرخش


    # background image list
    photo_list = ['imagess\\atom1.jpg', 'imagess\\atom2.jpg','imagess\\atom3.png']
    backgr = 0  # global index for image

    # Load initial background
    image = Image.open(photo_list[backgr])
    image = image.resize((800, 800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1, relwidth=1)

    # Define navigation buttons first (but don't place them yet)
    next_btn = Button(root, text=">>", font=('Segoe Print', 20, 'bold'), bg='pink', fg='red', command=lambda: change_bg(1))
    pr_btn = Button(root, text="<<", font=('Segoe Print', 20, 'bold'), bg='pink', fg='red', command=lambda: change_bg(-1))

    # Function to update the background
    def update_background():
        global bg_image, icon_photo, icon_label, angle

        # عکس اصلی پس‌زمینه
        img = Image.open(photo_list[backgr])
        img = img.resize((800, 800))
        bg_image = ImageTk.PhotoImage(img)
        bg_lbl.config(image=bg_image)
        bg_lbl.image = bg_image

        # دکمه‌ها
        if backgr > 0:
            pr_btn.place(x=15, y=230, height=40, width=50)
        else:
            pr_btn.place_forget()

        if backgr < len(photo_list) - 1:
            next_btn.place(x=735, y=230, height=40, width=50)
        else:
            next_btn.place_forget()

        # 🔁 اگه عکس دوم بود، آیکن بچرخه بیاد
        if backgr == 2:
            if not icon_label:
                icon_label = Label(root, bg='white')
                icon_label.place(x=350, y=450)  # جای دلخواه
            rotate_icon()
        else:
            if icon_label:
                icon_label.destroy()
                icon_label = None

    def rotate_icon():
        global icon_image_original, icon_photo, icon_label, angle
        if backgr == 2 and icon_label:
            rotated = icon_image_original.rotate(angle)
            icon_photo = ImageTk.PhotoImage(rotated)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
            angle = (angle + 10) % 360
            root.after(100, rotate_icon)  # هر ۰.۱ ثانیه یک دور


    # Function to change image index
    def change_bg(step):
        sound_play()
        global backgr
        backgr += step
        backgr = max(0, min(backgr, len(photo_list) - 1))
        update_background()

    # Initial button setup
    update_background()

    # Start the main loop
    root.mainloop()
