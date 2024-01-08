import mysql.connector

class Armazenar_botoes_03():
    """
    Classe responsável por gerenciar o armazenamento e manipulação de dados relacionados aos botões na tabela Botoes_03
    do banco de dados 'Cineplus'.

    Attributes
    ----------
    db_connection : mysql.connector.connection.MySQLConnection
        Conexão com o banco de dados MySQL.

    Methods
    -------
    drop_tabela_botoes_03():
        Verifica e exclui a tabela Botoes_03 se ela existir no banco de dados 'Cineplus'.
    criar_tabela_botoes_03():
        Cria a tabela Botoes_03 no banco de dados 'Cineplus' se ela ainda não existir.
    armazenar_botao_02(botao):
        Armazena um botão na tabela Botoes_03, substituindo se já existir e não tiver sido validado.
    buscar_botao_03(botao):
        Busca um botão na tabela Botoes_03 pelo seu nome (identificador único).
        Retorna um dicionário representando a linha correspondente, ou None se não encontrado.
    obter_todos_botoes_03():
        Obtém uma lista de todos os nomes de botões na tabela Botoes_03.
        Retorna None se não houver botões.
    obter_botoes_validos_03():
        Obtém uma lista de nomes de botões válidos (com o campo 'validar' igual a 1) na tabela Botoes_03.
        Retorna None se não houver botões válidos.
    atualizar_valido_03(nome_botao):
        Atualiza o valor 'validar' para 1 para um botão específico na tabela Botoes_03.
        Retorna True se a atualização for bem-sucedida, False em caso de erro.
    atualizar_cpf_03(novo_cpf):
        Atualiza o valor 'cpf' para o novo valor na tabela Botoes_03 onde 'cpf' é igual a 0.
        Retorna True se a atualização for bem-sucedida, False em caso de erro.
    obter_botoes_por_cpf_03(cpf):
        Obtém uma lista de nomes de botões associados a um CPF específico na tabela Botoes_03.
        Retorna None se nenhum botão estiver associado ao CPF ou em caso de erro.
    Exclui_Reserva_03(nome_botao):
        Exclui a linha correspondente a um botão específico na tabela Botoes_03.
        Retorna True se a exclusão for bem-sucedida, False em caso de erro.
    """

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
            cpf INT DEFAULT 0 NOT NULL,
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
        print('ENTROU EM BUSCAR BOTAO 3')
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


    def obter_todos_botoes_03(self):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes_03"
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


    def atualizar_valido_03(self, nome_botao):
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'validar' para 1 apenas para o botão específico
            update_query = "UPDATE Botoes_03 SET validar = 1 WHERE botao = %s"
            cursor.execute(update_query, (nome_botao,))
            self.db_connection.commit()
            
            print(f'Valor de "validar" atualizado para 1 para o botão {nome_botao}.')
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao atualizar "validar" para 1 para o botão {nome_botao}: {err}')
            return False
        finally:
            cursor.close()
    

    def atualizar_cpf_03(self, novo_cpf):
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'cpf' para o novo valor
            update_query = "UPDATE Botoes_03 SET cpf = %s WHERE cpf = 0"
            cursor.execute(update_query, (novo_cpf,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao atualizar "cpf" para {novo_cpf}: {err}')
            return False
        finally:
            cursor.close()

    def obter_botoes_por_cpf_03(self, cpf):
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes_03 WHERE cpf = %s"
        
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


    def Exclui_Reserva_03(self, nome_botao):
        cursor = self.db_connection.cursor()
        try:
            # Excluir a linha correspondente ao botão específico
            delete_query = "DELETE FROM Botoes_03 WHERE botao = %s"
            cursor.execute(delete_query, (nome_botao,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f'Erro ao excluir a linha para o botão {nome_botao}: {err}')
            return False
        finally:
            cursor.close()
