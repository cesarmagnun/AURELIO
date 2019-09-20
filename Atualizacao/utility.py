import pymysql

class ConnectionFactory:
        
    def getConnection(self):
        self.con = pymysql.connect("192.168.15.22", "cesar", "123", "teste")
        print("Conexao bem sucedida")
        return self.con



