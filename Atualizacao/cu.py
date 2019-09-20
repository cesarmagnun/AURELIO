import pyautogui
from Tkinter import *
from Read import SensorRFID
import time

def teste(e):
    SensorRFID()
ju = 1

if ju == 1:
    janela = Tk()
    janela.geometry("200x200")
    botao = Button(janela).pack()
    janela.bind("<Enter>", teste)
    janela.mainloop()
pyautogui.moveTo(20, 638, 4)




