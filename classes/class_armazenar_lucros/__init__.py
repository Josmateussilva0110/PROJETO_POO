import mysql.connector

class Armazenar_lucros:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.drop_tabela_lucros()
        self.cria_tabela_lucros()
    

    def drop_tabela_lucros(self):
        cursor = self.db_connection.cursor()

        try:
            # Verifica se a tabela Botoes existe antes de tentar excluí-la
            cursor.execute("SHOW TABLES LIKE 'Lucros'")
            table_exists = cursor.fetchone()

            if table_exists:
                # A tabela existe, então podemos tentar excluir
                drop_query = "DROP TABLE Lucros"
                cursor.execute(drop_query)
                self.db_connection.commit()
                # print("Tabela Botoes excluída com sucesso.")
            else:
                print("A tabela lucros não existe.")

        except mysql.connector.Error as err:
            print(f"Erro ao tentar excluir a tabela lucros: {err}")
            self.db_connection.rollback()
        finally:
            cursor.close()

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
        values = (valor,)
        try:
            cursor.execute(insert_query, values)
            self.db_connection.commit()
            valid = True 
            cursor.close()
        except mysql.connector.Error:
            self.db_connection.rollback()
            cursor.close()
        return valid


    def obter_lucro_total(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT MAX(lucro) FROM Lucros")
            maior_lucro = cursor.fetchone()[0] or 0.0
            return maior_lucro

        except mysql.connector.Error as err:
            # Handle the error appropriately
            print(f"Error: {err}")
            return 0.0