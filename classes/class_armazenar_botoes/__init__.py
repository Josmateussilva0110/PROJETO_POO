import mysql.connector

class Armazenar_botoes():
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.drop_tabela_botoes()
        self.criar_tabela_botoes()

    def drop_tabela_botoes(self):
        cursor = self.db_connection.cursor()

        try:
            # Verifica se a tabela Botoes existe antes de tentar excluí-la
            cursor.execute("SHOW TABLES LIKE 'Botoes'")
            table_exists = cursor.fetchone()

            if table_exists:
                # A tabela existe, então podemos tentar excluir
                drop_query = "DROP TABLE Botoes"
                cursor.execute(drop_query)
                self.db_connection.commit()
                # print("Tabela Botoes excluída com sucesso.")
            else:
                print("A tabela Botoes não existe.")

        except mysql.connector.Error as err:
            print(f"Erro ao tentar excluir a tabela Botoes: {err}")
            self.db_connection.rollback()
        finally:
            cursor.close()

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


    def obter_todos_botoes(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT * FROM Botoes"
        try:
            cursor.execute(select_query)
            result = cursor.fetchall()
            if result:
                botoes = [row[0] for row in result]
                cursor.close()
                return botoes
            else:
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None
