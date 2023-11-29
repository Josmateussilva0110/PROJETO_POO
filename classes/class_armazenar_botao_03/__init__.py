import mysql.connector

class Armazenar_botoes_03():
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.drop_tabela_botoes_03()
        self.criar_tabela_botoes_03()

    
    
    def drop_tabela_botoes_03(self):
        cursor = self.db_connection.cursor()

        try:
            # Verifica se a tabela Botoes_03 existe antes de tentar excluí-la
            cursor.execute("SHOW TABLES LIKE 'Botoes_03'")
            table_exists = cursor.fetchone()

            if table_exists:
                # A tabela existe, então podemos tentar excluir
                drop_query = "DROP TABLE Botoes_03"
                cursor.execute(drop_query)
                self.db_connection.commit()
                # print("Tabela Botoes_03 excluída com sucesso.")
            else:
                print("A tabela Botoes_03 não existe.")

        except mysql.connector.Error as err:
            print(f"Erro ao tentar excluir a tabela Botoes_03: {err}")
            self.db_connection.rollback()
        finally:
            cursor.close()



    def criar_tabela_botoes_03(self):
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_botoes = """
        CREATE TABLE IF NOT EXISTS Botoes_03 (
            botao VARCHAR(255),
            validar TINYINT(1) NOT NULL DEFAULT 0
        )
        """

        cursor.execute(criar_tabela_botoes)
        self.db_connection.commit()
        cursor.close()


    def armazenar_botao_03(self, botao):
        cursor = self.db_connection.cursor()
        
        # Verificar se o botão já existe no banco de dados
        existente = self.buscar_botao_03(botao)

        try:
            if existente:
                if existente["validar"] == 0:
                    # Se o botão já existe e ainda não foi validado, substituir
                    update_query = "UPDATE Botoes_03 SET validar = 0 WHERE botao = %s"
                    cursor.execute(update_query, (botao,))
                # Se existente["validar"] == 1, não fazemos nada (não substituímos)
            else:
                # Se o botão não existe, inserir um novo
                insert_query = "INSERT INTO Botoes_03(botao) VALUES (%s)"
                values = (botao,)
                cursor.execute(insert_query, values)

            self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            self.db_connection.rollback()
            cursor.close()
            return False


    def buscar_botao_03(self, botao):
        cursor = self.db_connection.cursor(dictionary=True)  # Usar dictionary=True para obter resultados como dicionários
        select_query = "SELECT * FROM Botoes_03 WHERE botao = %s"
        
        try:
            cursor.execute(select_query, (botao,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                return result
            else:
                return None
        except mysql.connector.Error as err:
            print(f'Erro ao buscar o botão {botao}: {err}')
            cursor.close()
            return None


    def obter_botoes_validos_03(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes_03 WHERE validar = 1"
        
        try:
            cursor.execute(select_query)
            result = cursor.fetchall()
            
            if result:
                botoes_validos = [row[0] for row in result]
                return botoes_validos
            else:
                return None

        except mysql.connector.Error as err:
            print(f'Erro ao obter botões válidos: {err}')
            return None
        finally:
            cursor.close() 
