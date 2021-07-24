import tkinter
import tkinter.messagebox
import random

from tkinter import *
from PIL import Image, ImageTk

def play_C():
    import PlayC

def play_S():
    #import PlayS
    import os
    os.popen("python PlayS.py")
    #os.system("cmd /c {python shape02.py}") 
    #exec(open("PlayS.py").read())
    
root = Tk()
root.title('SHAPES AND COLOURS DETECTING SYSTEM')
root.geometry('800x400')

def start():
    f1 = Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)

    Label(f1, text=' FUN WITH SHAPES AND COLOURS ',
          font="comicsansms 20 bold").grid(row=0, column=0, rowspan=2, columnspan=4)

    f1.pack()

    f2 = Frame(root, borderwidth=2)

    b1 = Button(f2, fg="black", text="  LEARN - SHAPES  ",
                font="comicsansms 10 bold", command=Learn_shapes)
    b1.grid(row=6, column=0, sticky=W, ipadx=20,
            ipady=20, rowspan=2, padx=20, pady=20)

    b2 = Button(f2, fg="black", text="LEARN - COLOURS",
                font="comicsansms 10 bold", command=Learn_colours)
    b2.grid(row=6, column=1, sticky=W, ipadx=20,
            ipady=20, rowspan=2, padx=20, pady=20)

    b3 = Button(f2, fg="black", text="PLAY - COLOURS",
                font="comicsansms 10 bold",command=play_C)
    b3.grid(row=8, column=0, sticky=W, ipadx=20,
            ipady=20, rowspan=2, padx=20, pady=20)
    b4 = Button(f2, fg="black", text=" PLAY - SHAPES",
                font="comicsansms 10 bold", command = play_S)
    b4.grid(row=8, column=1, sticky=E, ipadx=20,
            ipady=20, rowspan=2, padx=20, pady=20)

    f2.pack()


def Learn_shapes():
    root.destroy()
    t1 = Tk()
    t1.overrideredirect(TRUE)
    t1.geometry('1200x800')
    t1.title("LEARN DIFFERENT SHAPES")
    i1 = ImageTk.PhotoImage(Image.open("shapes2.png"))
    label1 = Label(image=i1)
    label1.pack()
    Checkbutton(t1, text='I have completed the learning part successfully', font="comicsansms 14")\
        .pack()
    button_quit = Button(
        t1, text='EXIT', font="comicsansms 14", command=t1.quit)
    button_quit.pack()
    t1.mainloop()


def Learn_colours():
    def end():
        t2.destroy()

    root.destroy()
    t2 = Tk()
    t2.overrideredirect(TRUE)
    t2.geometry('1200x800')
    t2.title("LEARN DIFFERENT COLOURS")
    i1 = ImageTk.PhotoImage(Image.open("colors1.png"))
    label1 = Label(image=i1)
    label1.pack()
    Checkbutton(t2, text='I have completed the learning part successfully', font="comicsansms 14")\
        .pack()
    button_quit = Button(
        t2, text='EXIT', font="comicsansms 14",bg='grey',command=end)
    button_quit.pack()
    t2.mainloop()


start()

root.mainloop()