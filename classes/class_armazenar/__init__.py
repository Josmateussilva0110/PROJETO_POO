import mysql.connector

class Armazenar:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.create_users_table()
        self.cria_gerente()
        self.inserir_gerente()
        self.tabela_filmes()

    def create_users_table(self):
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            email VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        self.db_connection.commit()
        cursor.close()

    def cria_gerente(self):
        # Use o banco de dados 'Cineplus'
        cursor = self.db_connection.cursor()
        cursor.execute("USE Cineplus")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS Gerencia (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            email VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        self.db_connection.commit()
        cursor.close()

    def tabela_filmes(self):
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

    def inserir_gerente(self):
        cursor = self.db_connection.cursor()
        nome = 'rai'
        cpf = '777'
        email = 'raileal_gerente@gmail.com'
        senha = '777'
        nome1 = 'mateus'
        cpf1 = '111'
        email1 = 'mateus_gerente@gmail.com'
        senha1 = '111'
        insert_query = "INSERT INTO Gerencia (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
        values = (nome, cpf, email, senha)
        insert_query_1 = "INSERT INTO Gerencia (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
        values1 = (nome1, cpf1, email1, senha1)
        cursor.execute(insert_query, values)
        cursor.execute(insert_query_1, values1)

        # Certifique-se de fechar os cursores
        cursor.close()

    def armazenar(self, pessoa):
        cursor = self.db_connection.cursor()

        # Verifica se o CPF já existe nos usuários
        check_user_query = "SELECT cpf FROM Usuarios WHERE cpf = %s"
        cursor.execute(check_user_query, (pessoa.cpf,))
        existing_user_cpf = cursor.fetchone()

        # Verifica se o CPF já existe na gerência
        check_gerencia_query = "SELECT cpf FROM Gerencia WHERE cpf = %s"
        cursor.execute(check_gerencia_query, (pessoa.cpf,))
        existing_gerencia_cpf = cursor.fetchone()

        if existing_user_cpf or existing_gerencia_cpf:
            # CPF já existe no banco de dados
            return False
        else:
            insert_query = "INSERT INTO Usuarios (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
            values = (pessoa.nome, pessoa.cpf, pessoa.email, pessoa.senha)
            try:
                cursor.execute(insert_query, values)
                self.db_connection.commit()
                cursor.close()
                return True
            except mysql.connector.Error as err:
                print("Erro ao inserir dados no banco de dados:", err)
                self.db_connection.rollback()
                cursor.close()
                return False
    
    def armazenar_filmes(self, filme):
        cursor = self.db_connection.cursor()

        insert_query = "INSERT INTO Filmes(nome_filme, ano, preco, classificacao, horario, tipo) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (filme._nome, filme._ano, filme._preco, filme._classificacao, filme._horarios, filme._tipo)
        try:
            cursor.execute(insert_query, values)
            self.db_connection.commit()
            cursor.close()  # Feche o cursor após a inserção bem-sucedida
            return True
        except mysql.connector.Error as err:
            print('passou aqui')
            print('Erro ao inserir dados no banco de dados:', err)
            self.db_connection.rollback()
            cursor.close()
            return False



    def verificar_login_Cliente(self, cpf, senha):
        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM Usuarios WHERE cpf = %s AND senha = %s"
        values = (cpf, senha)
        cursor.execute(select_query, values)
        result = cursor.fetchone()
        cursor.close()
        return result is not None
   

    def verificar_login_Ger(self, cpf, senha):
        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM Gerencia WHERE cpf = %s AND senha = %s"
        values = (cpf, senha)
        cursor.execute(select_query, values)
        result = cursor.fetchone()
        #self.db_connection.close()
        return result is not None
