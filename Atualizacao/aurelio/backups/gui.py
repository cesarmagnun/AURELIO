from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aurelio.persistence import QuestaoDao
from aurelio.entity import Questao

class TelaGrafica:  
    def __init__(self):
        self.window = Tk()
        self.window.title("Aurélio v.1")
        self.window.geometry("800x480")
        self.indice = 1
        self.vetResposta = []
        self.vTx_lblQuestao = StringVar()
        self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(self.indice)))
        self.lblQuestao = Label(self.window, wraplength=600, bd=1, relief="solid", font="Arial 16 bold",textvariable=self.vTx_lblQuestao).place(x=81, y=25, width=638, height=150)

        self.lblGrauCerteza = Label(self.window, bd=1, relief="flat", font="Arial 10 bold", text="Grau de certeza").place(x=82, y=200, width=116, height=34)
        self.lblGrauIncerteza = Label(self.window, bd=1, relief="flat", font="Arial 10 bold", text="Grau de incerteza").place(x=597, y=200, width=116, height=34)

        self.cbGrauCerteza = ttk.Combobox(self.window) 
        self.cbGrauCerteza['values'] = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
        self.cbGrauCerteza['font'] = ("arial 20 bold")
        self.cbGrauCerteza['justify'] = ("center")
        self.cbGrauCerteza.set(self.indice - 1)
        self.cbGrauCerteza.place(x=82, y=234, width=116, height=34)
        self.cbGrauCerteza.bind("<<ComboboxSelected>>", self.ativa_cbgrauincerteza)
        
        self.cbGrauIncerteza = ttk.Combobox(self.window)
        self.cbGrauIncerteza['values'] = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
        self.cbGrauIncerteza['font'] = ("arial 20 bold")
        self.cbGrauIncerteza['justify'] = ("center")
        self.cbGrauIncerteza['state'] = ("disabled")
        self.cbGrauIncerteza.set(self.indice - 1)
        self.cbGrauIncerteza.place(x=597, y=234, width=116, height=34)
        self.cbGrauIncerteza.bind("<<ComboboxSelected>>", self.ativa_btnavanca)
        
        
        self.vTx_lblNumQuestao = StringVar()
        self.vTx_lblNumQuestao.set(str(self.indice))
        self.lblNumQuestao = Label(self.window, bd=1, relief="flat", font="Arial 80 bold", textvariable=self.vTx_lblNumQuestao).place(x=325, y=257, width=150, height=150)
        
        
        
        
        self.btnVolta = Button(self.window)
        self.btnVolta['text'] = ("Voltar")
        self.btnVolta['bd'] = (1)
        self.btnVolta['relief'] = ("solid")
        self.btnVolta['state'] = ("disabled")
        self.btnVolta['command'] = (self.volta_questao)
        self.btnVolta.place(x=49, y=349, width=100, height=100)

        self.btnAvanca = Button(self.window)
        self.btnAvanca['text'] = ("Avançar")
        self.btnAvanca['bd'] = (1)
        self.btnAvanca['relief'] = ("solid")
        self.btnAvanca['state'] = ("disabled")
        self.btnAvanca['command'] = (self.avanca_questao)
        self.btnAvanca.place(x=649, y=349, width=100, height=100)
        
        self.window.mainloop()

    def avanca_questao(self):
        
       
        if self.indice == 9:
            self.btnAvanca['text'] = ("Finalizar")

        #1ªSituação - Lista vazia, posição atual vazia, adicionar elemento na 1º posição .   
        if self.vetResposta == []:
            questao = Questao()
            questao.set_graucerteza(float(self.cbGrauCerteza.get()))
            questao.set_grauincerteza(float(self.cbGrauIncerteza.get()))
            questao.set_status("Respondida")
            self.vetResposta.append(questao)
            self.indice += 1
            self.reset_combobox()
            self.btnAvanca['state'] = ("disabled")
            self.cbGrauIncerteza['state'] = ("disabled")
            self.vTx_lblNumQuestao.set(str(self.indice))
            self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(self.indice)))
        #2ªSituação - Lista não vazia - posição atual vazia, adicionar elemento na atual posição.   
        elif len(self.vetResposta) == self.indice - 1:
            questao = Questao()
            questao.set_graucerteza(float(self.cbGrauCerteza.get()))
            questao.set_grauincerteza(float(self.cbGrauIncerteza.get()))
            questao.set_status("Respondida")
            self.vetResposta.append(questao)
            self.indice += 1
            

            #2.1ªSituação - Lista completa - posição atual completa, solicitar gravar todas as informações.
            if self.indice == 11:
                if messagebox.askyesno("Nota de confirmação", "Deseja gravar todas as informações?") == True:
                    
                    QuestaoDao().insert(self.vetResposta)
                    messagebox.showinfo("Nota de êxito", "Informações gravadas com sucesso!")
                else:
                    self.indice -= 1
            
            else:        
                self.reset_combobox()
                self.btnAvanca['state'] = ("disabled")
                self.cbGrauIncerteza['state'] = ("disabled")
                self.vTx_lblNumQuestao.set(str(self.indice))
                self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(self.indice)))
        #3ªSituação - Lista não vazia - posição atual completa, atualizar elemento na posição atual.       
        else:
            self.vetResposta[self.indice-1].set_graucerteza(float(self.cbGrauCerteza.get()))
            self.vetResposta[self.indice-1].set_grauincerteza(float(self.cbGrauIncerteza.get()))
            self.indice += 1 #Mudança para a próxima posição
            
            #3.1ª - Lista completa - posição atual inexistente, solicitar gravar todas as informações. 
            if self.indice == 11:
                if messagebox.askyesno("Nota de confirmação", "Deseja gravar todas as informações?") == True:
                    messagebox.showinfo("Nota de êxito", "Informações gravadas com sucesso!")
                    for registro in range(0,10):
                        print(str(self.vetResposta[registro].get_graucerteza())+" "+str(self.vetResposta[registro].get_grauincerteza())+"\n")
                else:
                    self.indice -= 1
            #3.2ª - Lista não vazia - posição atual completa, carregar informações da posição atual.
            else:        
                if len(self.vetResposta) != self.indice-1:
                    self.cbGrauCerteza.set(float(self.vetResposta[self.indice-1].get_graucerteza()))
                    self.cbGrauIncerteza.set(float(self.vetResposta[self.indice-1].get_grauincerteza()))
                #3.1ª - Lista não vazia - posição atual completa, carregar informações da posição atual.    
                else:
                    self.reset_combobox()
                    self.btnAvanca['state'] = ("disabled")
                    self.cbGrauIncerteza['state'] = ("disabled")
                self.vTx_lblNumQuestao.set(str(self.indice))
                self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(self.indice)))    

           
                

 
            
        if self.indice != 1:
            self.btnVolta['state'] = ("active")
        

        
    def volta_questao(self):
        self.indice -= 1
        self.btnAvanca['state'] = ("active")
        self.cbGrauIncerteza['state'] = ("active")
        if self.indice != 10:
            self.btnAvanca['text'] = ("Avançar")
        if self.indice == 1:
            self.btnVolta['state'] = ("disabled")
        self.vTx_lblNumQuestao.set(str(self.indice))
        self.vTx_lblQuestao.set("".join(QuestaoDao().buscaQuestao(self.indice)))
        self.cbGrauCerteza.set(float(self.vetResposta[self.indice-1].get_graucerteza()))
        self.cbGrauIncerteza.set(float(self.vetResposta[self.indice-1].get_grauincerteza()))    
    def reset_combobox(self):
        self.cbGrauCerteza.set(0)
        self.cbGrauIncerteza.set(0)

    def ativa_cbgrauincerteza(self, e):
        self.cbGrauIncerteza['state'] = ("active")

    def ativa_btnavanca(self, e):
        self.btnAvanca['state'] = ("active")

    

TelaGrafica()






        





