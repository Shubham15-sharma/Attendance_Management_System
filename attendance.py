import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "./TrainingImageLabel/Trainner.yml"
)
trainimage_path = "./TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = (
    "./StudentDetails/studentdetails.csv"
)
attendance_path = "./Attendance"

window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#1c1c1c")  # Dark theme


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#1c1c1c")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="#1c1c1c",  # Dark background for the error window
        font=("Verdana", 16, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="#333333",  # Darker button color
        width=9,
        height=1,
        activebackground="red",
        font=("Verdana", 16, "bold"),
    ).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#1c1c1c",)
l1.place(x=470, y=10)


titl = tk.Label(
    window, text="CLASS VISION", bg="#1c1c1c", fg="yellow", font=("Verdana", 27, "bold"),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to CLASS VISION",
    bg="#1c1c1c",  # Dark background for the main text
    fg="yellow",  # Bright yellow text color
    bd=10,
    font=("Verdana", 35, "bold"),
)
a.pack()


ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("900x700")  # Increased window size
    ImageUI.configure(background="#2a2a2a")  # Lighter dark background for better visibility
    ImageUI.resizable(0, 0)
    
    # Create a scrollable frame
    main_frame = tk.Frame(ImageUI, bg="#2a2a2a")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # image and title
    titl = tk.Label(
        main_frame, text="Register Your Face", bg="#2a2a2a", fg="#00FF00", font=("Verdana", 30, "bold"),
    )
    titl.pack(pady=10)

    # heading
    a = tk.Label(
        main_frame,
        text="Enter the details",
        bg="#2a2a2a",  # Lighter dark background
        fg="yellow",  # Bright yellow text color
        bd=10,
        font=("Verdana", 24, "bold"),
    )
    a.pack(pady=5)

    # ER no
    lbl1 = tk.Label(
        main_frame,
        text="Enrollment No",
        width=15,
        height=1,
        bg="#2a2a2a",
        fg="cyan",
        bd=2,
        relief=RAISED,
        font=("Verdana", 14, "bold"),
    )
    lbl1.pack(pady=5)
    txt1 = tk.Entry(
        main_frame,
        width=30,
        bd=3,
        validate="key",
        bg="white",  # Bright white background for visibility
        fg="black",  # Dark text for contrast
        relief=SUNKEN,
        font=("Verdana", 14, "bold"),
    )
    txt1.pack(pady=5)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        main_frame,
        text="Name",
        width=15,
        height=1,
        bg="#2a2a2a",
        fg="cyan",
        bd=2,
        relief=RAISED,
        font=("Verdana", 14, "bold"),
    )
    lbl2.pack(pady=5)
    txt2 = tk.Entry(
        main_frame,
        width=30,
        bd=3,
        bg="white",  # Bright white background for visibility
        fg="black",  # Dark text for contrast
        relief=SUNKEN,
        font=("Verdana", 14, "bold"),
    )
    txt2.pack(pady=5)

    lbl3 = tk.Label(
        main_frame,
        text="Notification",
        width=15,
        height=1,
        bg="#2a2a2a",
        fg="cyan",
        bd=2,
        relief=RAISED,
        font=("Verdana", 14, "bold"),
    )
    lbl3.pack(pady=5)

    message = tk.Label(
        main_frame,
        text="",
        width=50,
        height=2,
        bd=3,
        bg="white",  # White background for visibility
        fg="black",  # Dark text for contrast
        relief=SUNKEN,
        font=("Verdana", 12, "bold"),
    )
    message.pack(pady=5)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # Button frame
    button_frame = tk.Frame(main_frame, bg="#2a2a2a")
    button_frame.pack(pady=10)

    # take Image button
    takeImg = tk.Button(
        button_frame,
        text="Take Image",
        command=take_image,
        bd=3,
        font=("Verdana", 14, "bold"),
        bg="green",
        fg="white",
        height=2,
        width=15,
        relief=RAISED,
    )
    takeImg.pack(side=tk.LEFT, padx=10)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        button_frame,
        text="Train Image",
        command=train_image,
        bd=3,
        font=("Verdana", 14, "bold"),
        bg="blue",
        fg="white",
        height=2,
        width=15,
        relief=RAISED,
    )
    trainImg.pack(side=tk.LEFT, padx=10)
    
    ImageUI.mainloop()


r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=100, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=600, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=1000, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=600, y=660)


window.mainloop()
