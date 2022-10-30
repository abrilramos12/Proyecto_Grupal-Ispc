from Conexion import Connection, user, password, host, database, port
from mysql.connector import Error
from Entitys import User

connection = Connection(user, password, host, database, port)

def connect_validation():
        if connection.db.is_connected():
                connection.cursor.close()
                connection.db.close()
                print('Conexión cerrada') 
                
class UserDao:

    def __init__(self):
        pass
    
    def create_user(User):
        sql = f"INSERT INTO user VALUES ())"
        try:
            connection.cursor.execute(sql)
            connection.db.commit()
        except Error as e:
            print(f'Error de insercion de usuario. Detalle: {e.msg}')
        finally:
            connect_validation()
                
    
    def search_user(id):
        sql = f"SELECT * FROM user WHERE id_user = '{id}'"
        try:
            connection.cursor.execute(sql)
            result = connection.cursor.fetchone()
            return result
        except Error as e:
            print(f"Error al consultar el id = {id}. Detalle: {e.msg}")
        finally:
            connect_validation()

    def update_user():
        pass

    def delete_user():
        pass

    
  