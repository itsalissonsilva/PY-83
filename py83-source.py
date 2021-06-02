import tkinter
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



root = tkinter.Tk()
root.geometry("400x680")
root.wm_title("PY-83")

#setting up graphing grid on canvas:
fig = Figure(figsize=(5, 3), dpi=100)
a = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tkinter.TOP)

#setting up interval for plotting:
x=np.linspace(-5,5,100)

#plotting function:
def plot():
    y = eval(e.get())
    lines = a.plot(x,y,'r')
    canvas.draw()

#setting up toolbar:
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP)



#adding number to the screen:
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))
    return

#four basic operations
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

#equal sign
def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

#clear entry and screen
def button_clear():
    e.delete(0,END)
    a.lines=[]
    canvas.draw()

#placing buttons on screen: 
button_1 = Button(root, text="1",padx=40,pady=20, command=lambda:button_click(1))
button_2 = Button(root, text="2",padx=40,pady=20, command=lambda:button_click(2))
button_3 = Button(root, text="3",padx=40,pady=20, command=lambda:button_click(3))

button_4 = Button(root, text="4",padx=40,pady=20, command=lambda:button_click(4))
button_5 = Button(root, text="5",padx=40,pady=20, command=lambda:button_click(5))
button_6 = Button(root, text="6",padx=40,pady=20, command=lambda:button_click(6))

button_7 = Button(root, text="7",padx=40,pady=20, command=lambda:button_click(7))
button_8 = Button(root, text="8",padx=40,pady=20, command=lambda:button_click(8))
button_9 = Button(root, text="9",padx=40,pady=20, command=lambda:button_click(9))

button_0 = Button(root, text="0",padx=40,pady=20, command=lambda:button_click(0))
button_equal = Button(root, text="=",padx=40,pady=20, command=button_equal, bg="#EA3C53")
button_divide = Button(root, text="÷",padx=40,pady=20, command=button_divide, bg="#89CFF0")

button_add = Button(root, text="+",padx=40,pady=20, command=button_add, bg="#89CFF0")
button_minus = Button(root, text="-",padx=40,pady=20, command=button_subtract, bg="#89CFF0")
button_mult = Button(root, text="×",padx=40,pady=20, command=button_multiply, bg="#89CFF0")
button_dot = Button(root, text=".",padx=40,pady=20, command=lambda:button_click("."))

button_clear = Button(root, text="Clear",padx=53,pady=4, command=button_clear)

button_plot = Button(root, text="Plot",padx=30,pady=4, command=plot, bg="#A0D6B4")



button_plot.place(x=300,y=310)

button_7.place(x=0,y=350)
button_8.place(x=100,y=350)
button_9.place(x=200,y=350)

button_4.place(x=0,y=420)
button_5.place(x=100,y=420)
button_6.place(x=200,y=420)

button_1.place(x=0,y=490)
button_2.place(x=100,y=490)
button_3.place(x=200,y=490)

button_0.place(x=0,y=560)
button_dot.place(x=100,y=560)
button_equal.place(x=200,y=560)

button_add.place(x=300,y=350)
button_minus.place(x=300,y=420)
button_mult.place(x=300,y=490)
button_divide.place(x=300,y=560)

button_clear.place(x=250,y=640)

#placing entry on the screen:
e = Entry(root, width = 45, borderwidth=5)
e.place(x=10,y=310)
#functions inputed on the entry are plotted on the screen, try something like x**2
#other functions need to be typed with reference to np as np.sin(x) or np.exp(x), for example


tkinter.mainloop()
