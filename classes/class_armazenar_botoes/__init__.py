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
            cpf INT DEFAULT 0 NOT NULL,
            botao VARCHAR(255),
            validar TINYINT(1) NOT NULL DEFAULT 0
        )
        """

        cursor.execute(criar_tabela_botoes)
        self.db_connection.commit()
        cursor.close()

        
    def armazenar_botao(self, botao):
        cursor = self.db_connection.cursor()
        
        # Verificar se o botão já existe no banco de dados
        existente = self.buscar_botao(botao)
        print('a busca aqui',existente)

        try:
            if existente:
                if existente["validar"] == 0:
                    # Se o botão já existe e ainda não foi validado, substituir
                    update_query = "UPDATE Botoes SET validar = 0 WHERE botao = %s"
                    cursor.execute(update_query, (botao,))
                # Se existente["validar"] == 1, não fazemos nada (não substituímos)
            else:
                # Se o botão não existe, inserir um novo
                insert_query = "INSERT INTO Botoes(botao) VALUES (%s)"
                print('inseri aqui',botao)
                values = (botao,)
                cursor.execute(insert_query, values)

            self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            self.db_connection.rollback()
            cursor.close()
            return False
        
    def buscar_botao(self, botao):
        print('ENTROU EM BUSCAR BOTAO')
        cursor = self.db_connection.cursor(dictionary=True)  # Usar dictionary=True para obter resultados como dicionários
        select_query = "SELECT * FROM Botoes WHERE botao = %s"
        print(select_query)
        
        try:
            cursor.execute(select_query, (botao,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                print('achou algo',result)
                return result
            else:
                return None
        except mysql.connector.Error as err:
            print(f'Erro ao buscar o botão {botao}: {err}')
            cursor.close()
            return None


    def obter_todos_botoes(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes"
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
        
    def obter_botoes_validos(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes WHERE validar = 1"
        
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
            
    def atualizar_valido(self, nome_botao):
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'validar' para 1 apenas para o botão específico
            update_query = "UPDATE Botoes SET validar = 1 WHERE botao = %s"
            cursor.execute(update_query, (nome_botao,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao atualizar "validar" para 1 para o botão {nome_botao}: {err}')
            return False
        finally:
            cursor.close()
            
    def atualizar_cpf(self, novo_cpf):
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'cpf' para o novo valor
            update_query = "UPDATE Botoes SET cpf = %s WHERE cpf = 0"
            cursor.execute(update_query, (novo_cpf,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao atualizar "cpf" para {novo_cpf}: {err}')
            return False
        finally:
            cursor.close()

    def obter_botoes_por_cpf(self, cpf):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes WHERE cpf = %s"
        
        try:
            cursor.execute(select_query, (cpf,))
            result = cursor.fetchall()

            if result:
                botoes_associados = [row[0] for row in result]
                return botoes_associados
            else:
                return None  # Retorna None se nenhum botão estiver associado ao CPF

        except mysql.connector.Error as err:
            print(f'Erro ao obter botões associados ao CPF {cpf}: {err}')
            return None  # Retorna None em caso de erro
        finally:
            cursor.close()
            
    def Exclui_Reserva(self, nome_botao):
        print('ENTROU EM EXCLUIR RESERVA')
        cursor = self.db_connection.cursor()
        try:
            # Excluir a linha correspondente ao botão específico
            delete_query = "DELETE FROM Botoes WHERE botao = %s"
            cursor.execute(delete_query, (nome_botao,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao excluir a linha para o botão {nome_botao}: {err}')
            return False
        finally:
            cursor.close()
