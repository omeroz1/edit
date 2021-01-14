from tkinter import *
import basic_edit
import datetime
from PIL import ImageTk
import PIL.Image
from tkinter import filedialog
import os
import shutil


def upload_image():
    upload_button = Button(step_2, text="Browse a File", command=file_dialog)
    upload_button.config(anchor="center")
    upload_button.grid(row=4, column=0, padx=10, pady=10)


def file_dialog():
    file_name = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                           filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    upload_lbl = Label(text="the image {} uploaded successfully!\nclick the 'lets go' button to start edit!" \
                       .format(file_name.split('/')[-1]))
    upload_lbl.grid(row=4, column=0, pady=15)
    # file_name = C:/Users/omero/OneDrive/desktop/images/DSCF1594.jpg
    nver_image = basic_edit.read_image(file_name)
    nver_image.resize((200*200))
    nver_image.show()


def time():
    date = datetime.datetime.now()
    if 6 < int(date.strftime('%H')) <= 12:
        return 'good morning!'
    elif 12 < int(date.strftime('%H')) <= 18:
        return 'good afternoon!'
    elif 18 < int(date.strftime('%H')) <= 20:
        return 'good evening!'
    elif 20 < int(date.strftime('%H')) < 24 or 0 < int(date.strftime('%H')) <= 6:
        return 'good night!'


def new_window1():
    """
    creates new gui window
    """
    global win1
    try:
        if win1.state() == "normal":
            win1.focus()
    except NameError as e:
        print(e)
    win1 = Toplevel()
    root.withdraw()
    win1.title("PEP - photo edit platform")
    win1.iconbitmap('gallery.ico')
    win1.geometry("500x600")
    win1["bg"] = "light blue"

    image_path = 'deni.jpg'
    image = basic_edit.read_image(image_path)

    hello_txt = "hello {}! and {}.\nlets edit the image!".format(name.get(), time())
    hello_lbl = Message(win1, text=hello_txt, fg="blue", width=1000, borderwidth=5)
    hello_lbl.config(font=("Fixedsys", 10))
    hello_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    help_win1 = LabelFrame(win1, text=" Quick Help ")
    help_win1.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=20, pady=20)
    help_lbl_win1 = Label(help_win1, text="MENU")
    help_lbl_win1.grid(row=0, sticky="WE")

    b1 = Button(win1, text="click for sharpness", command=lambda: basic_edit.sharpness_image(image), fg="black",
                bg="turquoise")
    b1.grid(row=1, column=0)

    b2 = Button(win1, text="click for contrast", command=lambda: basic_edit.contrast_image(image), fg="black",
                bg="turquoise")
    b2.grid(row=1, column=1)

    b3 = Button(win1, text="click for brightness", command=lambda: basic_edit.brightness_image(image), fg="black",
                bg="turquoise")
    b3.grid(row=1, column=2)

    img_lbl.grid(row=3, column=0)
    """img_path = 'C:/Users/omero/PycharmProjects/pythonProject6/{}/{}'.format('DF', img_name)
    img_og = ImageTk.PhotoImage(PIL.Image.open(img_path))
    new_img = basic_edit.resize_image(img_og, 200, 300)
    img_ver = []
    img_lbl = Label(win1, image=new_img)
    img_lbl.grid(row=3, column=0)"""

    win1.mainloop()


def submit_name():
    greet = "hello {}".format(name.get())
    name_lbl = Label(root, text=greet)
    name_lbl.grid()
    move_to_win1()


def move_to_win1():
    new_window1()


root = Tk()
root.title("PEP - photo edit platform")
root.iconbitmap('gallery.ico')
root["bg"] = "light blue"
root.geometry("600x400")
msg_txt = "Hello! Welcome to PEP - Photo Edit Platform.\nplease enter your name to continue"
name_lbl = Message(root, text=msg_txt, fg="blue", width=1000, borderwidth=5)
name_lbl.config(font=("Fixedsys", 5))
name_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

step_1 = LabelFrame(root, text=" 1. Enter Your Name: ")
step_1.grid(row=1, columnspan=7, sticky='W', padx=20, pady=5, ipadx=5, ipady=5)

name = Entry(step_1, fg="blue", borderwidth=10, width=30)
name.get()
name.grid(row=1, column=0, ipady=0)
"""
bname = Button(step_1, text="SUBMIT NAME", command=submit_name)
bname.config(anchor="center")
bname.grid(row=1, column=1, sticky="news")
"""
helpLf = LabelFrame(root, text=" Quick Help ")
helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=5, pady=5)
helpLbl = Label(helpLf, text="Please Enter Your Name\nand Upload the Image\nyou Want to edit.")
helpLbl.grid(row=0, sticky="WE")

step_2 = LabelFrame(root, text=" 2. Upload Your Image: ")
step_2.grid(row=2, columnspan=7, sticky='W', padx=20, pady=20, ipadx=5, ipady=5)
upload_image()

step_3 = LabelFrame(root, text=" 3. Lets Edit ! ")
step_3.grid(row=3, columnspan=7, sticky='W', padx=20, pady=5, ipadx=5, ipady=5)

b_to_win1 = Button(step_3, text="LETS GO!", command=submit_name)
b_to_win1.config(anchor="center")
b_to_win1.grid(row=3, column=1, padx=5, pady=5, sticky="news")

root.mainloop()
