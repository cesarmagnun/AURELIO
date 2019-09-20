from Tkinter import *
import time;
import datetime
import pygame, sys, random

pygame.init()
root = Tk()
root.title("Avaliacao Funcionario")

root.resizable(False, False)

root.configure(background='yellow')

FrameABC = Frame(root, bg="black", bd=5, relief= RIDGE)
FrameABC.grid()

FrameABC1 =Frame(FrameABC, bg="black", bd=5, relief= RIDGE)
FrameABC1.grid(row=0, column=0, columnspan=2, sticky=W)

FrameABC2 =Frame(FrameABC, bg="black", bd=5, relief= RIDGE)
FrameABC2.grid(row=2, column=0, columnspan=2, sticky=W)

FrameABC3 =Frame(FrameABC, bg="black", bd=5, relief= RIDGE)
FrameABC3.grid(row=1, column=0, columnspan=2, sticky=W)

Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

#=======================================================================================================================

lblDate = Label(FrameABC1, textvariable = Date1, font=('arial', 30, 'bold'),padx=9,pady=9,
                bd=14,bg="Cadet Blue", fg="Cornsilk", justify=CENTER).grid(row=0, column=0)

lblTitle = Label(FrameABC1, text = "\tAvaliacao Funcionario\t", font=('arial', 30, 'bold'),padx=9,pady=9,
                bd=14,bg="Cadet Blue", fg="Cornsilk", justify=CENTER).grid(row=0, column=1)

lblTime = Label(FrameABC1, textvariable = Time1, font=('arial', 30, 'bold'),padx=9,pady=9,
                bd=14,bg="Cadet Blue", fg="Cornsilk", justify=CENTER).grid(row=0, column=2)

#=======================================================================================================================
lbl1 = Button(FrameABC2, text = "01", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=1,columnspan=2)

lbl2 = Button(FrameABC2, text = "02", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=4,columnspan=2)

lbl3 = Button(FrameABC2, text = "03", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=7,columnspan=2)

lbl4 = Button(FrameABC2, text = "04", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=10,columnspan=2)

lbl5 = Button(FrameABC2, text = "05", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=13,columnspan=2)

lbl6 = Button(FrameABC2, text = "06", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=16,columnspan=2)

lbl7 = Button(FrameABC2, text = "07", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=19,columnspan=2)

lbl8 = Button(FrameABC2, text = "08", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=22,columnspan=2)

lbl9 = Button(FrameABC2, text = "09", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=CENTER).grid(row=0, column=25,columnspan=2)

lbl10 = Button(FrameABC2, text = "10", font=('arial', 20, 'bold'),padx=27,pady=9,
                bd=8,bg="red", fg="black",justify=RIGHT).grid(row=0, column=28,columnspan=10)
#=======================================================================================================================

lbl11 = Label(FrameABC3, text = "Risco1", font=('arial', 20, 'bold'),padx=540,pady=50,
                bd=14,bg="Cadet Blue", fg="Cornsilk",justify=CENTER).grid(row=0, column=0,columnspan=2)



root.mainloop()
