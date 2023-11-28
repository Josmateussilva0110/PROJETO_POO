import mysql.connector

class Armazenar_botoes_02():
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.drop_tabela_botoes_02()
        self.criar_tabela_botoes_02()

    
    
    def drop_tabela_botoes_02(self):
        cursor = self.db_connection.cursor()

        try:
            # Verifica se a tabela Botoes_02 existe antes de tentar excluí-la
            cursor.execute("SHOW TABLES LIKE 'Botoes_02'")
            table_exists = cursor.fetchone()

            if table_exists:
                # A tabela existe, então podemos tentar excluir
                drop_query = "DROP TABLE Botoes_02"
                cursor.execute(drop_query)
                self.db_connection.commit()
                # print("Tabela Botoes_02 excluída com sucesso.")
            else:
                print("A tabela Botoes_02 não existe.")

        except mysql.connector.Error as err:
            print(f"Erro ao tentar excluir a tabela Botoes_02: {err}")
            self.db_connection.rollback()
        finally:
            cursor.close()


    def criar_tabela_botoes_02(self):
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_botoes = """
        CREATE TABLE IF NOT EXISTS Botoes_02 (
            botao VARCHAR(255),
            validar TINYINT(1) NOT NULL DEFAULT 0
        )
        """

        cursor.execute(criar_tabela_botoes)
        self.db_connection.commit()
        cursor.close()


    def armazenar_botao_02(self, botao):
        cursor = self.db_connection.cursor()
        
        # Verificar se o botão já existe no banco de dados
        existente = self.buscar_botao_02(botao)

        try:
            if existente:
                if existente["validar"] == 0:
                    # Se o botão já existe e ainda não foi validado, substituir
                    update_query = "UPDATE Botoes_02 SET validar = 0 WHERE botao = %s"
                    cursor.execute(update_query, (botao,))
                # Se existente["validar"] == 1, não fazemos nada (não substituímos)
            else:
                # Se o botão não existe, inserir um novo
                insert_query = "INSERT INTO Botoes_02(botao) VALUES (%s)"
                values = (botao,)
                cursor.execute(insert_query, values)

            self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            self.db_connection.rollback()
            cursor.close()
            return False


    def buscar_botao_02(self, botao):
        cursor = self.db_connection.cursor(dictionary=True)  # Usar dictionary=True para obter resultados como dicionários
        select_query = "SELECT * FROM Botoes_02 WHERE botao = %s"
        
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


    def obter_todos_botoes_02(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes_02"
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
            print(f'Erro ao obter todos os botões: {err}')
            cursor.close()
            return None


    def obter_botoes_validos_02(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes_02 WHERE validar = 1"
        
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


    def atualizar_valido_02(self, nome_botao):
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'validar' para 1 apenas para o botão específico
            update_query = "UPDATE Botoes_02 SET validar = 1 WHERE botao = %s"
            cursor.execute(update_query, (nome_botao,))
            self.db_connection.commit()
            
            print(f'Valor de "validar" atualizado para 1 para o botão {nome_botao}.')
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao atualizar "validar" para 1 para o botão {nome_botao}: {err}')
            return False
        finally:
            cursor.close()
