from tkinter import *
import matplotlib.pyplot as plt
import fnmatch
import os
from tkinter import messagebox
def layout():
    #Setting up the window
    window = Tk()
    window.title("Temperature Plotter")
    window.geometry('350x150')
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

    def shift_one():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()

        for file in os.listdir('.'): #Check for file in directory
            if fnmatch.fnmatch(file, f"Temp_log_{y}_{m}_{d}*"):
                f = open(file,"r")
                l = f.readlines()
                f.close()
                x = []
                y = []
                x_s = []
                y_s = []
                for i in l:
                    sub = i.split("\t")
                    x += [float(sub[3]+"."+sub[4])]
                    y += [float(sub[6])]
                for i in range(len(x)):
                    if x[i]>=0 and x[i]<8:
                        x_s.append(x[i])
                        y_s.append(y[i])
                
                plt.xlabel("Time(hours)")
                plt.ylabel("Temperature(degree Celsius)")
                plt.title("Time vs Temperature")        
                plt.grid(True)
                plt.plot(x_s,y_s)
                plt.show()


    def shift_two():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()

        for file in os.listdir('.'): #Check for file in directory
            if fnmatch.fnmatch(file, f"Temp_log_{y}_{m}_{d}*"):
                f = open(file,"r")
                l = f.readlines()
                f.close()
                x = []
                y = []
                x_s = []
                y_s = []
                for i in l:
                    sub = i.split("\t")
                    x += [float(sub[3]+"."+sub[4])]
                    y += [float(sub[6])]
                for i in range(len(x)):
                    if x[i]>=8 and x[i]<16:
                        x_s.append(x[i])
                        y_s.append(y[i])
                
                plt.xlabel("Time(hours)")
                plt.ylabel("Temperature(degree Celsius)")
                plt.title("Time vs Temperature")
                plt.grid(True)
                plt.plot(x_s,y_s)
                plt.show()

    def shift_three():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()

        for file in os.listdir('.'): #Check for file in directory
            if fnmatch.fnmatch(file, f"Temp_log_{y}_{m}_{d}*"):
                f = open(file,"r")
                l = f.readlines()
                f.close()
                x = []
                y = []
                x_s = []
                y_s = []
                for i in l:
                    sub = i.split("\t")
                    x += [float(sub[3]+"."+sub[4])]
                    y += [float(sub[6])]
                for i in range(len(x)):
                    if x[i]>=16 and x[i]<24:
                        x_s.append(x[i])
                        y_s.append(y[i])
                        
                plt.xlabel("Time(hours)")
                plt.ylabel("Temperature(degree Celsius)")
                plt.title("Time vs Temperature")
                plt.grid(True)
                plt.plot(x_s,y_s)
                plt.show()


    btn1 = Button(window, text="Shift One", command=shift_one)
    btn1.grid(column=1, row=4)
    btn2 = Button(window, text="Shift Two", command=shift_two)
    btn2.grid(column=2, row=4)
    btn3 = Button(window, text="Shift Three", command=shift_three)
    btn3.grid(column=3, row=4)
    window.mainloop()
layout()
