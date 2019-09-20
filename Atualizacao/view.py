from Tkinter import *
import ttk
import tkMessageBox
from persistence import QuestaoDao
from model import Questao
from control import ViewController

class QuestionarioGUI:  

        
    def __init__(self): #Metodo resposanvel pela montagem da Tela Questionario Funcionarios
        
        self.listaResposta = [] #Lista responsavel pelas respostas do usuario
        self.indice = 1 #Variavel responsavel pelo indice da lista
        
    
        self.window = Tk()
        #self.window.iconbitmap('D:/Dados/Documentos/Faculdade/UNIP/TCC/IMAGENS/icon.ico')
        self.window.title("Questionario - Aurelio v.1")
        self.window.geometry("800x480")

        self.vTx_lblQuestao = StringVar()
        #Usar a classe controller para acessar o dao
        self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(self.indice)))

        self.lblQuestao = Label(self.window)
        self.lblQuestao['wraplength'] = 600
        self.lblQuestao['bd'] = 1
        self.lblQuestao['relief'] = "solid"
        self.lblQuestao['font'] = "Arial 16 bold"
        self.lblQuestao['text'] = self.vTx_lblQuestao.get()
        self.lblQuestao.place(x=81, y=25, width=638, height=150)
        
        #Criacao do Rotulo Grau Certeza
        self.lblGrauCerteza = Label(self.window, bd=1, relief="flat", font="Arial 10 bold", text="Grau de certeza").place(x=82, y=200, width=116, height=34)
        

        self.cbGrauCerteza = ttk.Combobox(self.window) 
        self.cbGrauCerteza['values'] = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
        self.cbGrauCerteza['font'] = ("arial 20 bold")
        self.cbGrauCerteza['justify'] = ("center")
        self.cbGrauCerteza.set(self.indice - 1)
        self.cbGrauCerteza.place(x=82, y=234, width=116, height=34)
        self.cbGrauCerteza.bind("<<ComboboxSelected>>", self.ativa_btnavanca)
        
        
        self.vTx_lblNumQuestao = StringVar()
        self.vTx_lblNumQuestao.set(str(self.indice)+'/'+str(ViewController().indiceQuestao()))
        self.lblNumQuestao = Label(self.window)
        self.lblNumQuestao['bd'] = 1
        self.lblNumQuestao['relief'] = "flat"
        self.lblNumQuestao['font'] = "Arial 60 bold"
        self.lblNumQuestao['text'] = self.vTx_lblNumQuestao.get()
        self.lblNumQuestao.place(x=325, y=257, width=150, height=150)
        
        
        self.btnVolta = Button(self.window)
        self.btnVolta['text'] = ("Voltar")
        self.btnVolta['bd'] = (1)
        self.btnVolta['relief'] = ("solid")
        self.btnVolta['state'] = ("disabled")
        self.btnVolta['command'] = (self.volta_questao)
        self.btnVolta.place(x=49, y=349, width=100, height=100)

        self.btnAvanca = Button(self.window)
        self.btnAvanca['text'] = ("Avancar")
        self.btnAvanca['bd'] = (1)
        self.btnAvanca['relief'] = ("solid")
        self.btnAvanca['state'] = ("disabled")
        self.btnAvanca['command'] = (self.avanca_questao)
        self.btnAvanca.place(x=649, y=349, width=100, height=100)

        self.window.mainloop()


    def avanca_questao(self):
        
       
        if self.indice == 15:
            self.btnAvanca['text'] = ("Finalizar")

        #1Situacao - Lista vazia, posicao atual vazia, adicionar elemento na 1 posicao .   
        if self.listaResposta == []:
            questao = Questao()
            questao.set_graucerteza(float(self.cbGrauCerteza.get()))
            #Remocao
            self.listaResposta.append(questao)
            self.indice += 1
            self.reset_combobox()
            self.btnAvanca['state'] = ("disabled")
            #Remocao
            
            self.update_labels(self.indice)
            
        #2Situacao - Lista nao vazia - posicao atual vazia, adicionar elemento na atual posicao.   
        elif len(self.listaResposta) == self.indice - 1:
            if self.indice == 16:
                if tkMessageBox.askyesno("Nota de confirmacao", "Deseja gravar todas as informacoes?") == True:
                    questao = Questao()
                    questao.set_graucerteza(float(self.cbGrauCerteza.get()))
                    self.listaResposta.append(questao)
                    
                    QuestaoDao().insert(self.listaResposta)
                    #tkMessageBox.showinfo("Nota de exito", "Informacoes gravadas com sucesso!")
                    #Bot fala
                    #Fechar janela
                    self.indice += 1
                
            else:
                questao = Questao()
                questao.set_graucerteza(float(self.cbGrauCerteza.get()))
                #Remocao
                self.listaResposta.append(questao)
                self.indice += 1
            
            
            #2.1Situacao - Lista completa - posicao atual completa, solicitar gravar todas as informacoes.

            
                   
                self.reset_combobox()
                self.btnAvanca['state'] = ("disabled")
                #Remocao
                self.update_labels(self.indice)
        #3Situacao - Lista nao vazia - posicao atual completa, atualizar elemento na posicao atual.       
        else:
            self.listaResposta[self.indice-1].set_graucerteza(float(self.cbGrauCerteza.get()))
            #Remocao
            self.indice += 1 #Mudanca para a proxima posicao
            
            #3.1 - Lista completa - posicao atual inexistente, solicitar gravar todas as informacoes. 
            if self.indice == 11:
                if tkMessageBox.askyesno("Nota de confirmacao", "Deseja gravar todas as informacoes?") == True:
                    QuestaoDao().insert(self.listaResposta)
                    tkMessageBox.showinfo("Nota de exito", "Informacoes gravadas com sucesso!")
                    for registro in range(0,10):
                        print(str(self.listaResposta[registro].get_graucerteza())+"\n")
                else:
                    self.indice -= 1
            #3.2 - Lista nao vazia - posicao atual completa, carregar informacoes da posicao atual.
            else:        
                if len(self.listaResposta) != self.indice-1:
                    self.cbGrauCerteza.set(float(self.listaResposta[self.indice-1].get_graucerteza()))
                    #Remocao
                #3.1 - Lista nao vazia - posicao atual completa, carregar informacoes da posicao atual.    
                else:
                    self.reset_combobox()
                    self.btnAvanca['state'] = ("disabled")
                    #Remocao
                self.update_labels(self.indice)    

        if self.indice != 1:
            if self.indice != 17:
                self.btnVolta['state'] = ("active")
            else:
                self.fecharJanela()
            
        print(self.indice)
        
    def volta_questao(self):
        self.indice -= 1
        self.btnAvanca['state'] = ("active")
        #Remocao
        if self.indice != 10:
            self.btnAvanca['text'] = ("Avancar")
        self.update_labels(self.indice)
        self.cbGrauCerteza.set(float(self.listaResposta[self.indice-1].get_graucerteza()))
        #Remocao   
    def reset_combobox(self):
        self.cbGrauCerteza.set(0)
        #Remocao

    #remocao

    def ativa_btnavanca(self, e):
        self.btnAvanca['state'] = ("active")

    def update_labels(self, i):
        #fazer isso com o objeto controler
        self.vTx_lblNumQuestao.set(str(i)+'/'+str(ViewController().indiceQuestao()))
        self.lblNumQuestao['text'] = self.vTx_lblNumQuestao.get()
        
        self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(i)))
        self.lblQuestao['text'] = self.vTx_lblQuestao.get()

    def fecharJanela(self):
        self.window.destroy()
        









        





