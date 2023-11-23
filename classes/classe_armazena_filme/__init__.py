import mysql.connector

class Armazenar_filmes:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cria_tabela_filmes()

    def cria_tabela_filmes(self):
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
        cursor = self.db_connection.cursor()
        valid = False
        
        # Obtém o próximo ID automaticamente
        #novo_id = self.obter_ultimo_id() + 1

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

    def marcar_filme_em_cartaz(self, filme_id,cartaz):
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
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM filmes WHERE em_cartaz = 1")
            filmes = cursor.fetchall()
            filme_strings = [f"ID: {filme[0]}\nNome: {filme[1]}\nAno: {filme[2]}\nPreço: {filme[3]}\nClassificação: {filme[4]}\nHorário: {filme[5]}\nEm Cartaz: {filme[6]}" for filme in filmes]
            return filme_strings
        except Exception as e:
            return []
