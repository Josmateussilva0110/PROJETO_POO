import mysql.connector

def configure_mysql_connection():
    """
    Configura uma conexão com um servidor MySQL.
    """
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="7319",
        )
        return mydb
    except mysql.connector.Error as err:
        return None
    
def create_database():
    """
    Cria o banco de dados 'Cineplus' se ele não existir.

    """
    mybd = configure_mysql_connection()
    cursor = mybd.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Cineplus")
