import tkinter as tk
from tkinter import *
from tkinter import ttk #css for tkinter
from PIL import Image, ImageTk
import time

LARGE_FONT=("Times New Roman",12)

class myapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #tk.Tk.iconbitmap(self,default="myicon.ico") #to add icons
        tk.Tk.wm_title(self, "My app")
        container = tk.Frame(self)
        self.attributes("-fullscreen", True)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

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

                #adding image to start page:
        logo = tk.PhotoImage(file="dalek.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=300,y=100,width=720,height=500)
        label = tk.Label(self,text="Are you a human?",font = LARGE_FONT)
        label.pack(pady=50,padx=100)

        

        button = ttk.Button(self, text="Yes", command = lambda:controller.show_frame(PageOne))
        button.place(x=500,y=650)

        button2 = ttk.Button(self, text="No", command = quit)
        button2.place(x=700,y=650)


class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        for i in range(50):
            label = tk.Label(self,text="EXTERMINATE!    EXTERMINATE!    EXTERMINATE!    EXTERMINATE!    EXTERMINATE!    EXTERMINATE!",font = LARGE_FONT)
            label.pack(pady=10,padx=10)

        
        #my_img = ImageTk.PhotoImage(Image.open("image.png"))
        #my_label = Label(image=my_img)
        #my_label.pack()


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page 02",font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command = lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One", command = lambda:controller.show_frame(PageOne))
        button2.pack()        



        

app = myapp()

app.mainloop()
