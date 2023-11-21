import mysql.connector

class Armazenar_botoes():
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.criar_tabela_botoes()

    def criar_tabela_botoes(self):
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_botoes = """
        CREATE TABLE IF NOT EXISTS Botoes (
            botao VARCHAR(255)
        )
        """

        cursor.execute(criar_tabela_botoes)
        self.db_connection.commit()
        cursor.close()


    def armazenar_botoes(self, botao):
        cursor = self.db_connection.cursor()
        valid = False

        insert_query = "INSERT INTO Botoes(botao) VALUES (%s)"
        values = (botao, )
        try:
            cursor.execute(insert_query, values)
            self.db_connection.commit()
            valid = True 
            cursor.close()
        except mysql.connector.Error:
            self.db_connection.rollback()
            cursor.close()
        return valid
    

    def buscar_botao(self, botao):
        cursor = self.db_connection.cursor()

        select_query = "SELECT * FROM Botoes WHERE botao = %s"
        try:
            cursor.execute(select_query, (botao,))
            result = cursor.fetchone()
            if result:
                achou = result
                cursor.close()
                return achou
            else:
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None
