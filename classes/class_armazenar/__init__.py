import mysql.connector

class Armazenar:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.create_users_table()
        self.cria_gerente()
        self.inserir_gerente1()

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

    def inserir_gerente1(self):
        cursor = self.db_connection.cursor()
        cpf = '777'  # CPF do gerente a ser inserido
        select_query = "SELECT cpf FROM Gerencia WHERE cpf = %s"
        cursor.execute(select_query, (cpf,))
        existing_gerente_cpf = cursor.fetchone()
        
        cursor1 = self.db_connection.cursor()
        cpf1 = '111'  # CPF do gerente a ser inserido
        select_query1 = "SELECT cpf FROM Gerencia WHERE cpf = %s"
        cursor1.execute(select_query1, (cpf1,))
        existing_gerente_cpf1 = cursor1.fetchone()   
        if not existing_gerente_cpf:
            nome = 'rai'
            email = 'raileal_gerente@gmail.com'
            senha = '777'
            insert_query = "INSERT INTO Gerencia (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
            values = (nome, cpf, email, senha)
            cursor.execute(insert_query, values)
            
        if not existing_gerente_cpf1:
            nome1 = 'mateus'
            email1 = 'mateus_gerente@gmail.com'
            senha1 = '111'
            insert_query1 = "INSERT INTO Gerencia (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
            values1 = (nome1, cpf1, email1, senha1)
            cursor1.execute(insert_query1, values1)

        # Certifique-se de fechar o cursor
        cursor.close()

    def armazenar(self, pessoa):
        cursor = self.db_connection.cursor()

        # Verifica se o CPF já existe nos usuários
        check_user_query = "SELECT cpf FROM Usuarios WHERE cpf = %s"
        cursor.execute(check_user_query, (pessoa._cpf,))
        existing_user_cpf = cursor.fetchone()

        # Verifica se o CPF já existe na gerência
        check_gerencia_query = "SELECT cpf FROM Gerencia WHERE cpf = %s"
        cursor.execute(check_gerencia_query, (pessoa._cpf,))
        existing_gerencia_cpf = cursor.fetchone()

        if existing_user_cpf or existing_gerencia_cpf:
            # CPF já existe no banco de dados
            return False
        else:
            insert_query = "INSERT INTO Usuarios (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
            values = (pessoa._nome, pessoa._cpf, pessoa._email, pessoa._senha)
            try:
                cursor.execute(insert_query, values)
                self.db_connection.commit()
                cursor.close()
                return True
            except mysql.connector.Error as err:
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


    def buscar_cliente_cpf(self, cpf):
        cursor = self.db_connection.cursor()
        select_query = "SELECT nome FROM Usuarios WHERE cpf = %s"
        values = (cpf,)
        cursor.execute(select_query, values)
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None

