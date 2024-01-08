import mysql.connector

class Armazenar_filmes:
    """
    Classe responsável por gerenciar o armazenamento e manipulação de dados relacionados a filmes na tabela Filmes
    do banco de dados 'Cineplus'.

    Attributes
    ----------
    db_connection : mysql.connector.connection.MySQLConnection
        Conexão com o banco de dados MySQL.

    Methods
    -------
    cria_tabela_filmes()
        Cria a tabela Filmes no banco de dados 'Cineplus' se ela ainda não existir.
    armazenar_filmes(filme)
        Armazena informações sobre um filme na tabela Filmes.
        Retorna True se o armazenamento for bem-sucedido, False em caso de erro.
    buscar_filme_por_id(filme_id)
        Busca informações sobre um filme com base no seu ID na tabela Filmes.
        Retorna uma string formatada com os detalhes do filme ou None se não encontrado.
    buscar_filme_em_cartaz_por_id(filme_id)
        Busca informações sobre um filme em cartaz com base no seu ID na tabela Filmes.
        Retorna uma string formatada com os detalhes do filme ou None se não encontrado.
    buscar_dados_filmes(filme_id)
        Busca informações básicas sobre um filme com base no seu ID na tabela Filmes.
        Retorna uma string formatada com os detalhes do filme ou None se não encontrado.
    buscar_horarios_id(filme_id)
        Obtém a lista de horários de exibição de um filme com base no seu ID na tabela Filmes.
        Retorna a lista de horários ou None se não encontrado.
    obter_todos_filmes()
        Obtém uma lista formatada com os detalhes de todos os filmes na tabela Filmes.
        Retorna uma lista de strings ou uma lista vazia em caso de erro.
    marcar_filme_em_cartaz(filme_id, cartaz)
        Marca ou desmarca um filme como "em cartaz" na tabela Filmes.
        Retorna True se a operação for bem-sucedida, False em caso de erro.
    verificar_filme_em_cartaz(filme_id)
        Verifica se um filme está atualmente em cartaz com base no seu ID na tabela Filmes.
        Retorna True se estiver em cartaz, False se não estiver ou em caso de erro.
    obter_todos_filmes_em_cartaz()
        Obtém uma lista formatada com os detalhes de todos os filmes atualmente em cartaz na tabela Filmes.
        Retorna uma lista de strings ou uma lista vazia em caso de erro.
    contar_filmes_cadastrados()
        Conta o número total de filmes cadastrados na tabela Filmes.
        Retorna o número total de filmes cadastrados ou 0 em caso de erro.
    contar_filmes_em_cartaz()
        Conta o número total de filmes atualmente em cartaz na tabela Filmes.
        Retorna o número total de filmes em cartaz ou 0 em caso de erro.
    somar_precos_total_tela_1()
        Soma os preços de todos os filmes na tabela Filmes.
        Retorna o total de preços ou 0 em caso de erro.
    """
        
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cria_tabela_filmes()

    def cria_tabela_filmes(self):
        """"Cria a tabela Filmes no banco de dados se ela ainda não existir."""

        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        criar_tabela_filmes = """
        CREATE TABLE IF NOT EXISTS Filmes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_filme VARCHAR(100) NOT NULL,
            ano INT NOT NULL,
            preco FLOAT NOT NULL,
            classificacao VARCHAR(100) NOT NULL,
            horario VARCHAR(255) NOT NULL,
            em_cartaz TINYINT(1) NOT NULL DEFAULT 0
        )
        """

        cursor.execute(criar_tabela_filmes)
        self.db_connection.commit()
        cursor.close()

    def armazenar_filmes(self, filme):
        """
        Armazena informações sobre um filme na tabela Filmes.

        Parameters
        ----------
        filme : objeto Filme
            O objeto Filme contendo as informações do filme a ser armazenado.

        Returns
        -------
        bool
            True se o armazenamento for bem-sucedido, False em caso de erro.
        """

        cursor = self.db_connection.cursor()
        valid = False
        
        insert_query = "INSERT INTO Filmes(nome_filme, ano, preco, classificacao,horario) VALUES (%s, %s, %s, %s, %s)"
        values = (filme._nome, filme._ano, filme._preco, filme._classificacao, filme._horarios)
        try:
            cursor.execute(insert_query, values)
            self.db_connection.commit()
            valid = True 
            cursor.close()
        except mysql.connector.Error:
            self.db_connection.rollback()
            cursor.close()
        return valid
    

    def buscar_filme_por_id(self, filme_id):
        """
        Busca informações sobre um filme com base no seu ID na tabela Filmes.

        Parameters
        ----------
        filme_id : int
            O ID do filme a ser pesquisado na tabela Filmes.

        Returns
        -------
        str or None
            Uma string formatada com os detalhes do filme se encontrado, ou None se não encontrado.
        """

        cursor = self.db_connection.cursor()

        # Query to fetch the film with the given ID
        select_query = "SELECT * FROM Filmes WHERE id = %s"

        try:
            cursor.execute(select_query, (filme_id,))
            result = cursor.fetchone()
            if result:
                list_result5 = result[5].split()
                print(list_result5)
                # Film with the provided ID found, format its information as a string
                filme_info = f"ID: {result[0]}\nNome: {result[1]}\nAno: {result[2]}\nPreço: {result[3]}\nClassificação: {result[4]}\nHorário: {result[5]}\nEm Cartaz: {result[6]}"
                cursor.close()
                return filme_info
            else:
                # No film with the provided ID was found
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None
    

    def buscar_filme_em_cartaz_por_id(self, filme_id):
        """
        Busca informações sobre um filme em cartaz com base no seu ID na tabela Filmes.

        Parameters
        ----------
        filme_id : int
            O ID do filme a ser pesquisado na tabela Filmes.

        Returns
        -------
        str or None
            Retorna uma string formatada com os detalhes do filme ou None se não encontrado.
        """

        cursor = self.db_connection.cursor()

        # Query to fetch the film with the given ID
        select_query = "SELECT * FROM Filmes WHERE id = %s AND em_cartaz = 1"

        try:
            cursor.execute(select_query, (filme_id,))
            result = cursor.fetchone()
            if result:
                # Film with the provided ID found, format its information as a string
                filme_info = f"ID: {result[0]}\nNome: {result[1]}\nAno: {result[2]}\nPreço: {result[3]}\nClassificação: {result[4]}\nHorário: {result[5]}\nEm Cartaz: {result[6]}"
                cursor.close()
                return filme_info
            else:
                # No film with the provided ID was found
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None
    


    def buscar_dados_filmes(self, filme_id):
        """
        Busca informações básicas sobre um filme com base no seu ID na tabela Filmes.

        Parameters
        ----------
        filme_id : int
            O ID do filme a ser pesquisado na tabela Filmes.

        Returns
        -------
        str or None
            Retorna uma string formatada com os detalhes do filme ou None se não encontrado.
        """

        cursor = self.db_connection.cursor()

        # Query to fetch the film with the given ID
        select_query = "SELECT * FROM Filmes WHERE id = %s"

        try:
            cursor.execute(select_query, (filme_id,))
            result = cursor.fetchone()
            if result:
                # Film with the provided ID found, format its information as a string
                filme_info = f"ID: {result[0]} Nome: {result[1]} Ano: {result[2]} Preço: {result[3]} Classificação: {result[4]}"
                cursor.close()
                return filme_info
            else:
                # No film with the provided ID was found
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None
    

    def buscar_horarios_id(self, filme_id):
        """
        Obtém a lista de horários de exibição de um filme com base no seu ID na tabela Filmes.

        Parameters
        ----------
        filme_id : int
            O ID do filme a ser pesquisado na tabela Filmes.

        Returns
        -------
        list or None
            Retorna a lista de horários ou None se não encontrado.
        """

        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM Filmes WHERE id = %s"

        try:
            cursor.execute(select_query, (filme_id,))
            result = cursor.fetchone()
            if result:
                horario_info = result[5]  
                cursor.close()
                horarios_list = horario_info.split(', ')
                return horarios_list
            else:
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None

        

    def obter_todos_filmes(self):
        """
        Obtém uma lista formatada com os detalhes de todos os filmes na tabela Filmes.

        Returns
        -------
        list or None
        Retorna uma lista de strings ou uma lista vazia em caso de erro.

        """

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM Filmes")
            filmes = cursor.fetchall()
            filme_strings = [
                f"ID: {filme[0]}\nNome: {filme[1]}\nAno: {filme[2]}\nPreço: {filme[3]}\nClassificação: {filme[4]}\nHorário: {filme[5]}\nEm Cartaz: {filme[6]}"
                for filme in filmes
            ]
            return filme_strings
        except mysql.connector.Error as err:
            return []

    def marcar_filme_em_cartaz(self, filme_id, cartaz):
        """
        Marca ou desmarca um filme como "em cartaz" na tabela Filmes.

        Parameters
        ----------
        filme_id : int
            O ID do filme a ser marcado ou desmarcado.
        cartaz : int
            Valor 1 para marcar o filme como "em cartaz" e 0 para desmarcar.

        Returns
        -------
        bool
            True se a operação for bem-sucedida, False em caso de erro.
        """

        try:
            cursor = self.db_connection.cursor()
            # Atualize o banco de dados para marcar o filme como "em cartaz"
            if cartaz == 1:
                sql = f"UPDATE Filmes SET em_cartaz = 1 WHERE id = {filme_id}"
                cursor.execute(sql)
                self.db_connection.commit()
            else:
                sql = f"UPDATE Filmes SET em_cartaz = 0 WHERE id = {filme_id}"
                cursor.execute(sql)
                self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            return False
        
    def verificar_filme_em_cartaz(self, filme_id):
        """
        Verifica se um filme está atualmente em cartaz com base no seu ID na tabela Filmes.

        Parameters
        ----------
        filme_id : int
            O ID do filme a ser verificado.

        Returns
        -------
        bool
            True se o filme estiver em cartaz, False se não estiver ou em caso de erro.
        """

        try:
            cursor = self.db_connection.cursor()

            # Consulta para verificar se o filme está em cartaz
            query = "SELECT em_cartaz FROM Filmes WHERE id = %s"
            cursor.execute(query, (filme_id,))

            resultado = cursor.fetchone()

            # Se o resultado for encontrado e em_cartaz for 1, o filme está em cartaz
            if resultado and resultado[0] == 1:
                return True
            else:
                return False

        except mysql.connector.Error as err:
            return False

        finally:
            cursor.close()
            
    def obter_todos_filmes_em_cartaz(self):
        """
        Obtém uma lista formatada com os detalhes de todos os filmes atualmente em cartaz na tabela Filmes.

        Returns
        -------
        list
        Retorna uma lista de strings ou uma lista vazia em caso de erro.

        """

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM filmes WHERE em_cartaz = 1")
            filmes = cursor.fetchall()
            filme_strings = [f"ID: {filme[0]}\nNome: {filme[1]}\nAno: {filme[2]}\nPreço: {filme[3]}\nClassificação: {filme[4]}\nHorário: {filme[5]}\nEm Cartaz: {filme[6]}" for filme in filmes]
            return filme_strings
        except Exception as e:
            return []
        
    def contar_filmes_cadastrados(self):
        """
        Conta o número total de filmes cadastrados na tabela Filmes.

        Returns
        -------
        int
        Retorna o número total de filmes cadastrados ou 0 em caso de erro.

        """

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM Filmes")
            count = cursor.fetchone()[0]
            return count
        except mysql.connector.Error as err:
            return 0
        finally:
            cursor.close()
    
    def contar_filmes_em_cartaz(self):
        """
        Conta o número total de filmes atualmente em cartaz na tabela Filmes.

        Returns
        -------
        int 
        Retorna o número total de filmes em cartaz ou 0 em caso de erro

        """

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM Filmes WHERE em_cartaz = 1")
            count = cursor.fetchone()[0]
            return count
        except mysql.connector.Error as err:
            return 0
        finally:
            cursor.close()

    def somar_precos_total_tela_1(self):
        """
        Soma os preços de todos os filmes na tabela Filmes.

        Returns
        -------
        int 
        Retorna o total de preços ou 0 em caso de erro.
        
        """
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT SUM(preco) FROM Filmes")
            total_preco = cursor.fetchone()[0]
            return total_preco
        except mysql.connector.Error as err:
            return 0
        finally:
            cursor.close()
