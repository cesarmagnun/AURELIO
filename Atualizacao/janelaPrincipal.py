from Tkinter import *


class Principal:

    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("800x400")
        self.botao = Button(self.janela)
        self.botao['text'] = 'teste'
        self.botao.pack()
        self.botao['command'] = self.fechar
        self.mensagem()
        self.janela.mainloop()

    def fechar(self):
        self.janela.destroy()

    def mensagem(self):
        print('vsf')


Principal()
