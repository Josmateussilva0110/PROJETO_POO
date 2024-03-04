import mysql.connector

class Armazenar_botoes_02():
    """
    Classe responsável por gerenciar o armazenamento e manipulação de dados relacionados aos botões na tabela Botoes_02
    do banco de dados 'Cineplus'.

    Attributes
    ----------
    db_connection : mysql.connector.connection.MySQLConnection
        Conexão com o banco de dados MySQL.

    Methods
    -------
    drop_tabela_botoes_02():
        Verifica e exclui a tabela Botoes_02 se ela existir no banco de dados 'Cineplus'.
    criar_tabela_botoes_02():
        Cria a tabela Botoes_02 no banco de dados 'Cineplus' se ela ainda não existir.
    armazenar_botao_02(botao):
        Armazena um botão na tabela Botoes_02, substituindo se já existir e não tiver sido validado.
    buscar_botao_02(botao):
        Busca um botão na tabela Botoes_02 pelo seu nome (identificador único).
        Retorna um dicionário representando a linha correspondente, ou None se não encontrado.
    obter_todos_botoes_02():
        Obtém uma lista de todos os nomes de botões na tabela Botoes_02.
        Retorna None se não houver botões.
    obter_botoes_validos_02():
        Obtém uma lista de nomes de botões válidos (com o campo 'validar' igual a 1) na tabela Botoes_02.
        Retorna None se não houver botões válidos.
    atualizar_valido_02(nome_botao):
        Atualiza o valor 'validar' para 1 para um botão específico na tabela Botoes_02.
        Retorna True se a atualização for bem-sucedida, False em caso de erro.
    atualizar_cpf_02(novo_cpf):
        Atualiza o valor 'cpf' para o novo valor na tabela Botoes_02 onde 'cpf' é igual a 0.
        Retorna True se a atualização for bem-sucedida, False em caso de erro.
    obter_botoes_por_cpf_02(cpf):
        Obtém uma lista de nomes de botões associados a um CPF específico na tabela Botoes_02.
        Retorna None se nenhum botão estiver associado ao CPF ou em caso de erro.
    Exclui_Reserva_02(nome_botao):
        Exclui a linha correspondente a um botão específico na tabela Botoes_02.
        Retorna True se a exclusão for bem-sucedida, False em caso de erro.
    """
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.drop_tabela_botoes_02()
        self.criar_tabela_botoes_02()

    
    
    def drop_tabela_botoes_02(self):
        """Verifica e exclui a tabela Botoes_02 se ela existir no banco de dados"""

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

        except mysql.connector.Error as err:
            self.db_connection.rollback()
        finally:
            cursor.close()


    def criar_tabela_botoes_02(self):
        """Cria a tabela Botoes_02 no banco de dados se ela ainda não existir"""

        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_botoes = """
        CREATE TABLE IF NOT EXISTS Botoes_02 (
            cpf INT DEFAULT 0 NOT NULL,
            botao VARCHAR(255),
            validar TINYINT(1) NOT NULL DEFAULT 0
        )
        """

        cursor.execute(criar_tabela_botoes)
        self.db_connection.commit()
        cursor.close()


    def armazenar_botao_02(self, botao):
        """Armazena um botão na tabela Botoes_02, substituindo se já existir e não tiver sido validado
        Returns
        -------
        bool
        Retorna True se o botão for armazenado com sucesso, False em caso de erro.
        """

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
        """Busca um botão na tabela Botoes_02 pelo seu nome (identificador único).
        Retorna um dicionário representando a linha correspondente, ou None se não encontrado.
        
        Returns
        -------
        dict or None
        Retorna um dicionário representando a linha correspondente na tabela Botoes_02 se o botão for encontrado, 
        ou None se não for encontrado.
        """
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
            cursor.close()
            return None


    def obter_todos_botoes_02(self):
        """
        Obtém uma lista de todos os nomes de botões na tabela Botoes_02.
        Retorna None se não houver botões

        Returns
        -------
        list or None
        Retorna uma lista de identificadores únicos de botões se houver botões na tabela Botoes_02, 
        ou None se não houver botões.
        """
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
            cursor.close()
            return None


    def obter_botoes_validos_02(self):
        """
        Obtém uma lista de nomes de botões válidos (com o campo 'validar' igual a 1) na tabela Botoes_02.
        Retorna None se não houver botões válidos
        
        Returns
        -------
        list or None
        Retorna uma lista de identificadores únicos de botões válidos se houver botões válidos na tabela Botoes_02, 
        ou None se não houver botões válidos.
        """
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
            return None
        finally:
            cursor.close() 


    def atualizar_valido_02(self, nome_botao):
        """
        Atualiza o valor 'validar' para 1 para um botão específico na tabela Botoes_02.
        Retorna True se a atualização for bem-sucedida, False em caso de erro
        
        Returns
        -------
        bool
        Retorna True se a atualização for bem-sucedida, False em caso de erro.
        """
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'validar' para 1 apenas para o botão específico
            update_query = "UPDATE Botoes_02 SET validar = 1 WHERE botao = %s"
            cursor.execute(update_query, (nome_botao,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            return False
        finally:
            cursor.close()
    

    def atualizar_cpf_02(self, novo_cpf):
        """
        Atualiza o valor 'cpf' para o novo valor na tabela Botoes_02 onde 'cpf' é igual a 0.
        Retorna True se a atualização for bem-sucedida, False em caso de erro
        
        Returns
        -------
        bool
        Retorna True se a atualização for bem-sucedida, False em caso de erro.
        """
        cursor = self.db_connection.cursor()

        try:
            # Atualizar o valor de 'cpf' para o novo valor
            update_query = "UPDATE Botoes_02 SET cpf = %s WHERE cpf = 0"
            cursor.execute(update_query, (novo_cpf,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            return False
        finally:
            cursor.close()

    def obter_botoes_por_cpf_02(self, cpf):
        """
        Obtém uma lista de nomes de botões associados a um CPF específico na tabela Botoes_02.
        Retorna None se nenhum botão estiver associado ao CPF ou em caso de erro
        
        Returns
        -------
        list or None
        Retorna uma lista de identificadores únicos de botões associados ao CPF se houver algum na tabela Botoes_02, 
        ou None se nenhum botão estiver associado ao CPF ou em caso de erro.
        """
        cursor = self.db_connection.cursor()

        select_query = "SELECT botao FROM Botoes_02 WHERE cpf = %s"
        
        try:
            cursor.execute(select_query, (cpf,))
            result = cursor.fetchall()

            if result:
                botoes_associados = [row[0] for row in result]
                return botoes_associados
            else:
                return None  # Retorna None se nenhum botão estiver associado ao CPF

        except mysql.connector.Error as err:
            return None  # Retorna None em caso de erro
        finally:
            cursor.close()


    def Exclui_Reserva_02(self, nome_botao):
        """
        Exclui a linha correspondente a um botão específico na tabela Botoes_02.
        Retorna True se a exclusão for bem-sucedida, False em caso de erro
        
        Returns
        -------
        bool
        Retorna True se a exclusão for bem-sucedida, False em caso de erro.
        """
        cursor = self.db_connection.cursor()
        try:
            # Excluir a linha correspondente ao botão específico
            delete_query = "DELETE FROM Botoes_02 WHERE botao = %s"
            cursor.execute(delete_query, (nome_botao,))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            return False
        finally:
            cursor.close()
