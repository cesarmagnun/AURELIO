from utility import ConnectionFactory

class QuestaoDao:

    def buscaQuestao(self, id):
        self.cf = ConnectionFactory()
        self.con = self.cf.getConnection()
        self.cur = self.con.cursor()
        self.cur.execute("SELECT descricao FROM ameaca WHERE codigo = "+str(id))
        self.recset = self.cur.fetchall()
        
        for self.registers in self.recset:
            return self.registers


    def insert(self, lista):
        respostas = []
        indice = 0
        for aux in lista:
            
            aux = lista[indice].get_graucerteza()
            print(aux)
            respostas.append(lista[indice].get_graucerteza())
            print(respostas[indice])
            indice = indice+1
            
        self.cf = ConnectionFactory()
        self.con  = self.cf.getConnection()
        self.cur = self.con.cursor()
        self.cur.execute("INSERT INTO respostasFunc VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (respostas)) 
        self.con.commit()
        self.con.close()
    

    def indiceQuestao(self):
        self.cf = ConnectionFactory().getConnection()
        self.cur = self.cf.cursor()
        self.cur.execute("SELECT fn_contadorAmeaca()")
        self.recset = self.cur.fetchall()

        for self.registers in self.recset:
            return self.registers

#lista = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,7]
#QuestaoDao().insert(lista)
