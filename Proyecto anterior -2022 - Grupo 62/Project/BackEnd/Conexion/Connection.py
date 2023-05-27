import mysql.connector
# Variables Globales de conexión
config = {
    'user': 'root',
    'password' : 'root',
    'database' : 'capacit',
    'host' : 'localhost',
    'port' : '3306'    
}
class Connection:
    def __init__(self, **config):
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()
        print('Conexión establecida')
        
        
        
