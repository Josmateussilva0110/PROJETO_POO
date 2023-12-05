import mysql.connector

class Armazenar_lucros:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cria_tabela_lucros()

    def cria_tabela_lucros(self):
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_filmes = """
        CREATE TABLE IF NOT EXISTS Lucros (
            lucro FLOAT NOT NULL
        )
        """

        cursor.execute(criar_tabela_filmes)
        self.db_connection.commit()
        cursor.close()


    def armazenar_lucro(self, valor):
        cursor = self.db_connection.cursor()
        valid = False

        insert_query = "INSERT INTO Lucros(lucro) VALUES (%s)"
        values = (valor)
        try:
            cursor.execute(insert_query, values)
            self.db_connection.commit()
            valid = True 
            cursor.close()
        except mysql.connector.Error:
            self.db_connection.rollback()
            cursor.close()
        return valid
