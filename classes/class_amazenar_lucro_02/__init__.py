import mysql.connector

class Armazenar_lucros_02:
    """
    Classe responsável por gerenciar o armazenamento de dados de lucro_2 no banco de dados.

    Attributes
    ----------
    db_connection: Conexão com o banco de dados MySQL.

    Methods
    -------
    drop_tabela_lucros_02:
        Exclui do banco de dados a tabala lucros_02
    cria_tabela_lucros_02:
        Cria no banco de dados a tabala lucros_02
    armazenar_lucro_02(self, valor):
        Armazena no banco de dados a tabala lucros_02
    obter_lucro_total_02:
        Obtem o lucro total da tabela lucro_total_2

    """
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.drop_tabela_lucros_02()
        self.cria_tabela_lucros_02()
    

    def drop_tabela_lucros_02(self):
        """
        Exclui a tabela 'Lucros_02' do banco de dados, se ela existir.

        """
        cursor = self.db_connection.cursor()

        try:
            # Verifica se a tabela Botoes existe antes de tentar excluí-la
            cursor.execute("SHOW TABLES LIKE 'Lucros_02'")
            table_exists = cursor.fetchone()

            if table_exists:
                # A tabela existe, então podemos tentar excluir
                drop_query = "DROP TABLE Lucros_02"
                cursor.execute(drop_query)
                self.db_connection.commit()

        except mysql.connector.Error as err:
            self.db_connection.rollback()
        finally:
            cursor.close()

    def cria_tabela_lucros_02(self):
        """
        Cria a tabela 'Lucros_02' no banco de dados 'Cineplus', se ela não existir.
        """
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_filmes = """
        CREATE TABLE IF NOT EXISTS Lucros_02 (
            lucro FLOAT NOT NULL
        )
        """

        cursor.execute(criar_tabela_filmes)
        self.db_connection.commit()
        cursor.close()

    def armazenar_lucro_02(self, valor, flag):
        """
        Armazena o valor do lucro no banco de dados 'Lucros_02', atualizando ou inserindo conforme necessário.
        
        Returns
        -------
        bool
        Retorna True se o lucro for armazenado com sucesso, False se não houver lucro ou em caso de erro.
        """
        cursor = self.db_connection.cursor()
        valid = False
        cursor.execute("SELECT COUNT(*) FROM Lucros_02")
        count = cursor.fetchone()[0]

        if count == 0:
            insert_query = "INSERT INTO Lucros_02(lucro) VALUES (%s)"
            values = (valor,)
        else:
            cursor.execute("SELECT lucro FROM Lucros_02")
            lucro_existente = cursor.fetchone()[0]
            if flag == '1':
                novo_lucro = lucro_existente - float(valor)
            else:
                novo_lucro = lucro_existente + float(valor)
            update_query = "UPDATE Lucros_02 SET lucro = %s"
            values = (novo_lucro,)
            insert_query = None
        try:
            if insert_query:
                cursor.execute(insert_query, values)
            else:
                cursor.execute(update_query, values)
            self.db_connection.commit()
            valid = True
        except mysql.connector.Error as err:
            self.db_connection.rollback()
        finally:
            cursor.close()

        return valid


    def obter_lucro_total_02(self):
        """
        Retorna o maior valor de lucro armazenado na tabela 'Lucros_02'.
        
        Returns
        -------
        float
        O maior valor de lucro armazenado na tabela 'Lucros_02'. Retorna 0.0 se ocorrer um erro ou se não houver registros.
        
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT MAX(lucro) FROM Lucros_02")
            maior_lucro = cursor.fetchone()[0] or 0.0
            return maior_lucro

        except mysql.connector.Error as err:
            # Handle the error appropriately
            return 0.0
