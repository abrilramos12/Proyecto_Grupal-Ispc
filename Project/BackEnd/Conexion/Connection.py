import mysql.connector
# Variables Globales de conexión
user = 'root'
password = 'root'
host = 'localhost'
database = 'capacit'
port = '3306'


class Connection:
    def __init__(self, user, password, host, database, port):
        self.db = mysql.connector.connect(user, password, host, database, port)
        self.cursor = self.db.cursor()
        print('Conexión establecida')
