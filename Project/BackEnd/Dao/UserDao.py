import sys
sys.path.append('./Conexion')
from Conexion.Connection import Connection, user, password, host, database, port

from mysql.connector import Error

connection = Connection(user, password, host, database, port)

def connect_validation():
        if connection.db.is_connected():
                connection.cursor.close()
                connection.db.close()
                print('Conexión cerrada') 
                
class UserDao:

    def __init__(self):
        pass
    
    def save_user():
        sql = f"INSERT INTO user VALUES ('1','Nicolás','Ramos', 'jnramos','jnicolas.ramos10@gmail.com','1234', 1 , 'ADMIN', NULL, NULL, NULL))"
        try:
            connection.cursor.execute(sql)
            connection.db.commit()
            print('Guardado correcto')
        except Error as e:
            print(f'Error de insercion de usuario. Detalle: {e.msg}')
        finally:
            connect_validation()
                
    
    def find_user(id):
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

    
  
user_dao = UserDao()

user_dao.save_user()