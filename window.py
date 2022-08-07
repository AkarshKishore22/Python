from tkinter import *
from tkinter import ttk
import datetime as dt

win= Tk()
win.title("Display Current Date")
win.geometry("700x350")
date = dt.datetime.now()

win.geometry("550x350")
def open_win():
    
   new= Toplevel(win)
   new.geometry("550x350")
   new.title("New Window")
   
   Label(new, text="Hey bro, how ya doin'?", font=('Lora 20 bold')).pack(pady=40)
   label = Label(new, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20")
   label.pack(pady=20)
Label(win, text= "Click the window below to open", font= ('Arial 18 bold')).pack(pady=40)

ttk.Button(win, text="Open", command=open_win).pack()
win.mainloop()