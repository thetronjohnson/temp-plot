from tkinter import *
import matplotlib.pyplot as plt
import fnmatch
import os
def layout():
    #Setting up the window
    window = Tk()
    window.title("Temperature Plotter")
    window.geometry('200x150')
    #Setting Up the input area
    year = Label(window, text="Enter The Year")
    month = Label(window, text="Enter The Month")
    date = Label(window, text="Enter The Date")

    year.grid(column=1, row=1)
    month.grid(column=1, row=2)
    date.grid(column=1, row=3)

    year_txt = Entry(window,width=10)
    year_txt.grid(column=2, row=1)
    month_txt = Entry(window,width=10)
    month_txt.grid(column=2, row=2)
    date_txt = Entry(window,width=10)
    date_txt.grid(column=2, row=3)

    def clicked():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()

        for file in os.listdir('.'): #Check for file in directory
            if fnmatch.fnmatch(file, f"Temp_log_{y}_{m}_{d}*"):
                f = open(file,"r")
                

    btn = Button(window, text="Enter", command=clicked)
    btn.grid(column=1, row=5)
    window.mainloop()
layout()
