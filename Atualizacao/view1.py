from Tkinter import *
import ttk
import tkMessageBox
import pyautogui
from persistence import QuestaoDao
from model import Questao
from Read import SensorRFID

class AvaliacaoGUI:

    def __init__(self):
        self.window = Tk()
        #self.window.iconbitmap('D:/Dados/Documentos/Faculdade/UNIP/TCC/IMAGENS/icon.ico')
        self.window.title("Avaliacao de Funcionarios - Aurelio v.1")
        self.window.geometry("800x480")

        #self.imageAurelio = PhotoImage(file='/media/pi/ESD-USB1/AurelioQuestionariodeFuncionarios/Atualizacao/logo.png')
        #self.lblLogo = Label(self.window, image=self.imageAurelio)
        #self.lblLogo.imageAurelio = self.imageAurelio
        #self.lblLogo['bd'] = (1)
        #self.lblLogo['relief'] = ("solid")
        #self.lblLogo.place(x=195, y=28, width=413, height=216)
                                  
        self.var = StringVar()
        self.var.set("20/40")
        self.lblRespondido = Label(self.window, bd=1, relief="solid", font="Arial 50 bold", textvariable=self.var).place(x=275, y=265, width=251, height=151)


        self.txtRg = Entry(self.window)
        self.txtRg['bd'] = (1)
        self.txtRg['relief'] = ("solid")
        self.txtRg.place(x=360, y=430, width=166, height=27)
        self.txtRg.focus_set()
        self.button = Button(self.window)
        self.button['text'] = 'Teste'
        self.button['relief'] = 'solid'
        self.button.place(x=275, y=430, width=73, height=27)
        self.button['command'] = self.form
        #self.window.bind("<Enter>", self.form)
        #pyautogui.moveTo(716, 406)
 
        self.window.mainloop()

        
    def form(self):
        SensorRFID()

AvaliacaoGUI()

