from tkinter import *

root = Tk()
root.title("PLAY SHAPES GAME")
root.geometry('1400x800+0+0')
root.config(bg='black')
def select(event):
    b= event.widget
    value=b['text']
    for i in range(10):
        if value == correct_answers[i]: 
            #shapelabel1.config(image=questions[i+1])           
            option1.config(text=first_option[i+1])
            option2.config(text=second_option[i+1])
            option3.config(text=third_option[i+1])
            option4.config(text=forth_option[i+1])
            shapelabel1.config(image=questions[i+1])
            

        if value not in correct_answers:
           def close():
              root1.destroy()

           root1 = Toplevel()
           root1.config(bg='black')

           loseLable1=Label(root1, text="SORRY!",font=('arial',40,'bold'),bg='black',fg='white')
           loseLable1.pack()
           loseLable2= Label(root1, text="YOU LOST", font=('arial', 40, 'bold'), bg='black', fg='white')
           loseLable2.pack()

           TryAgain=Button(root1,text='Try Again',font=('arial', 10, 'bold'),bg='black',fg='white')
           TryAgain.pack()

           close = Button(root1, text='CLOSE', font=('arial', 10, 'bold'), bg='black', fg='white',command=close)
           close.pack()

           root1.mainloop()

           break


correct_answers=['TRIANGLE','CIRCLE'  ,'SQUARE' ,'PENTAGON','RECTANGLE','KITE'   ,'OCTAGON','DECAGON' ,'ELLIPSE','HEPTAGON']

first_option=['RIGHTANGLE','TRIANGLE','POLYGON','PENTAGON','HEXAGON'  ,'CIRCLE' ,'OCTAGON','DECAGON' ,'OVAL'   ,'NONAGON']

second_option=['POLYGON'   ,'CIRCLE'  ,'TRINGLE','SQUARE'  ,'RECTANGLE','HEXAGON','OVAL'   ,'NONAGON' ,'ELLIPSE','SEVENGON']

third_option=['TRIANGLE'   ,'EGG'     ,'OVAL'   ,'DIAMOND' ,'POLYGON'  ,'KITE'   ,'ELIPSEE','OCTAGON' ,'ARC'    ,'HEPTAGON']

forth_option=['SQUAARE'    ,'OVAL'    ,'SQUARE' ,'HEXAGON' ,'TRINGLE'  ,'HYPERBOLA' ,'HEXAGON','PARABOLA','PARABOLA','SEPTAGON']


leftframe=Frame(root,bg='black',bd=0)
leftframe.grid(row=0,column=0,padx=20)

rightframe=Frame(root,bg='black',pady=10,bd=0)
rightframe.grid(row=0,column=1,padx=90)

topframe=Frame(leftframe,bg='black',bd=0)
topframe.grid(row=0,column=0)

centerframe=Frame(leftframe,bg='black',bd=0)
centerframe.grid(row=1,column=0)

bottomframe=Frame(leftframe,bg='black',bd=0)
bottomframe.grid(row=2,column=0)

imghint = PhotoImage(file='hints.png')
hintbtn=Button(centerframe,image=imghint,bg='black',activebackground='black',width=150,height=50,bd=0)
hintbtn.grid(row=1,column=2,padx=20)

title=Label(topframe,text='SHAPES DETECTION GAME',font="comicsansms 30 bold",bg='black',fg='white',bd=0)
title.grid(row=0,column=1,columnspan=2)

pointimg= PhotoImage(file='point.png')
pointlabel = Label(rightframe,image=pointimg,bd=0)
pointlabel.grid(row=0,column=0)

shapeimg=PhotoImage(file='shape.png')
shapelabel =Label(centerframe,image=shapeimg,bd=0)
shapelabel.grid(row=0,column=0,columnspan=2)

shapeimg1=PhotoImage(file='01.png')
shapelabel1 =Label(centerframe,image=shapeimg1,bd=0)
shapelabel1.grid(row=0,column=0,columnspan=2)
shapelabel1.place(x=70,y=20)

shapeimg2=PhotoImage(file='02.png')
#shapelabel2 =Label(centerframe,image=shapeimg2,bd=0)
#shapelabel2.place(x=70,y=20)

shapeimg3=PhotoImage(file='03.png')
#shapelabel3 =Label(centerframe,image=shapeimg3,bd=0)
#shapelabel3.place(x=70,y=20)

shapeimg4=PhotoImage(file='04.png')
#shapelabel4 =Label(centerframe,image=shapeimg4,bd=0)
#shapelabel4.place(x=70,y=20)

shapeimg5=PhotoImage(file='05.png')
#shapelabel5 =Label(centerframe,image=shapeimg5,bd=0)
#shapelabel5.place(x=70,y=20)

shapeimg6=PhotoImage(file='06.png')
#shapelabel6 =Label(centerframe,image=shapeimg6,bd=0)
#shapelabel6.place(x=70,y=20)

shapeimg7=PhotoImage(file='07.png')
#shapelabel7 =Label(centerframe,image=shapeimg7,bd=0)
#shapelabel7.place(x=70,y=20)

shapeimg8=PhotoImage(file='08.png')
#shapelabel8 =Label(centerframe,image=shapeimg8,bd=0)
#shapelabel8.place(x=70,y=20)

shapeimg9=PhotoImage(file='09.png')
#shapelabel9 =Label(centerframe,image=shapeimg9,bd=0)
#shapelabel9.place(x=70,y=20)

shapeimg10=PhotoImage(file='10.png')
#shapelabel10 =Label(centerframe,image=shapeimg10,bd=0)
#shapelabel10.place(x=70,y=20)

questions=[shapeimg1,shapeimg2,shapeimg3,shapeimg4,shapeimg5,shapeimg6,shapeimg7,shapeimg8,shapeimg9,shapeimg10]

optionimg=PhotoImage(file='option.png')
optionlabel =Label(bottomframe,image=optionimg,bd=0)
optionlabel.grid(row=0,column=0)

labelA=Label(bottomframe,text="A: ",bg='black',fg='white',font="comicsansms 25 bold")
labelA.place(x=40,y=39)

labelB=Label(bottomframe,text="B: ",bg='black',fg='white',font="comicsansms 25 bold")
labelB.place(x=400,y=39)

labelC=Label(bottomframe,text="C: ",bg='black',fg='white',font="comicsansms 25 bold")
labelC.place(x=40,y=170)

labelD=Label(bottomframe,text="D: ",bg='black',fg='white',font="comicsansms 25 bold")
labelD.place(x=400,y=170)

option1=Button(bottomframe,text=first_option[0],bg='black',fg='white',font="comicsansms 25 bold",bd=0,activebackground='black',cursor='hand2')
option1.place(x=80,y=30)

option2=Button(bottomframe,text=second_option[0],bg='black',fg='white',font="comicsansms 25 bold",bd=0,activebackground='black',cursor='hand2')
option2.place(x=460,y=30)

option3=Button(bottomframe,text=third_option[0],bg='black',fg='white',font="comicsansms 25 bold",bd=0,activebackground='black',cursor='hand2')
option3.place(x=80,y=160)

option4=Button(bottomframe,text=forth_option[0],bg='black',fg='white',font="comicsansms 25 bold",bd=0,activebackground='black',cursor='hand2')
option4.place(x=460,y=160)

option1.bind('<Button-1>',select)
option2.bind('<Button-1>',select)
option3.bind('<Button-1>',select)
option4.bind('<Button-1>',select)

root.mainloop()