import matplotlib
matplotlib.use("TkAgg")
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import *
from tkinter import ttk

LARGE_FONT=("Times New Roman",12)
x=np.linspace(-5,5,100)


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #tk.Tk.iconbitmap(self,default="myicon.ico") #to add icons
        tk.Tk.wm_title(self, "My app")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GraphPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        label = tk.Label(self,text="Ed. App - Start Page",font = LARGE_FONT)
        label.pack(pady=10,padx=10)


        button3 = ttk.Button(self, text="Go to graph page ->", command = lambda:controller.show_frame(GraphPage))
        button3.pack()




class GraphPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        

        e = Entry(self, width =50)
        e.pack()
        label = tk.Label(self,text="Graph your function!",font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command = lambda:controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        def myClick():
           # y = e.get() i'd like something like this to work, instead of line below
            y = eval(e.get())
            a.plot(x,y,'r')
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                    
               

        button4 = ttk.Button(self, text="plot", command = myClick)
        button4.pack()





        

app = MyApp()
app.mainloop()
