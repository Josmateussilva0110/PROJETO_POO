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
            classificacao INT NOT NULL,
            horario VARCHAR(200) NOT NULL,
            tipo VARCHAR(10) NOT NULL
        )
        """
        cursor.execute(criar_tabela_filmes)
        self.db_connection.commit()
        cursor.close()
        
    def obter_ultimo_id(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(id) FROM Filmes")
        max_id = cursor.fetchone()[0]
        cursor.close()
        return max_id

    def armazenar_filmes(self, filme):
        cursor = self.db_connection.cursor()
        max_id = self.obter_ultimo_id()
        
        novo_id = max_id - 1 if max_id is not None else 1

        insert_query = "INSERT INTO Filmes(id, nome_filme, ano, preco, classificacao, horario, tipo) VALUES (%s,%s, %s, %s, %s, %s, %s)"
        values = (novo_id,filme._nome, filme._ano, filme._preco, filme._classificacao, filme._horarios, filme._tipo)
        try:
            cursor.execute(insert_query, values)
            self.db_connection.commit()
            cursor.close()  # Feche o cursor após a inserção bem-sucedida
            return True
        except mysql.connector.Error as err:
            self.db_connection.rollback()
            cursor.close()
            return False
        

    def verificar_filme(self, filme_id):
        cursor = self.db_connection.cursor()

        # Consulta para verificar se o filme com o ID fornecido existe
        select_query = "SELECT * FROM Filmes WHERE id = %s"
        
        try:
            cursor.execute(select_query, (filme_id,))
            result = cursor.fetchone()
            
            if result:
                # O filme com o ID fornecido foi encontrado, imprima suas informações
                cursor.close()
                return True
            else:
                # Nenhum filme com o ID fornecido foi encontrado
                cursor.close()
                return False
        except mysql.connector.Error as err:
            cursor.close()
            return False
        
    def buscar_filme_por_id(self, filme_id):
        cursor = self.db_connection.cursor()

        # Query to fetch the film with the given ID
        select_query = "SELECT * FROM Filmes WHERE id = %s"

        try:
            cursor.execute(select_query, (filme_id,))
            result = cursor.fetchone()

            if result:
                # Film with the provided ID found, format its information as a string
                filme_info = f"ID: {result[0]}\nNome: {result[1]}\nAno: {result[2]}\nPreço: {result[3]}\nClassificação: {result[4]}\nHorário: {result[5]}\nTipo: {result[6]}"
                cursor.close()
                print(filme_info)
                return filme_info
            else:
                # No film with the provided ID was found
                cursor.close()
                return None
        except mysql.connector.Error as err:
            cursor.close()
            return None
        
    def excluir_filmes(self, filme_id):
        cursor = self.db_connection.cursor()
        # Consulta para excluir o filme com base no ID
        delete_query = "DELETE FROM Filmes WHERE id = %s"

        try:
            cursor.execute(delete_query, (filme_id,))
            self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            self.db_connection.rollback()
            cursor.close()
            return False
        
    def obter_todos_filmes(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM Filmes")
            filmes = cursor.fetchall()
            filme_strings = [f"ID: {filme[0]}, Nome: {filme[1]}, Ano: {filme[2]}, Preço: {filme[3]}, Classificação: {filme[4]}, Horário: {filme[5]}, Tipo: {filme[6]}" for filme in filmes]
            return filme_strings
        except mysql.connector.Error as err:
            return []
        
        
    

        






