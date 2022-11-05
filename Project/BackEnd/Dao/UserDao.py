from Conexion.Connection import Connection, config
from mysql.connector import Error
from Entitys.User import User

connection = Connection(**config)


def connect_validation():
    if connection.db.is_connected():
        connection.cursor.close()
        connection.db.close()
        print('Conexión cerrada')


class UserDao:

    def __init__(self):
        pass
        # CREATE
    def save_user(self, user):
        if isinstance(user, User):
            data = tuple(user.__dict__.values())
        sql = "INSERT INTO user (id_user, first_name, last_name, username, email, password, active, role, create_time, user_git, user_linkedin) VALUES (%s, %s, %s ,%s ,%s , %s, %s, %s, %s, %s, %s)"
        try:
            connection.cursor.execute(sql, data)
            connection.db.commit()
            print('Guardado correcto')
        except Error as e:
            print(f'Error de insercion de usuario. Detalle: {e.msg}')
        finally:
            connect_validation()
    # READ
    def find_user(self, id):
        sql = f"SELECT * FROM user WHERE id_user = {id}"
        try:
            connection.cursor.execute(sql)
            result = connection.cursor.fetchone()
            return result
        except Error as e:
            print(f"Error al consultar el id = {id}. Detalle: {e.msg}")
        finally:
            connect_validation()
    # UPDATE
    def update_username(self, id, username):
        sql = f"UPDATE user SET username = '{username}' WHERE id_user = '{id}'"
        try:
            connection.cursor.execute(sql)
            connection.db.commit()
            print('Actualización correcta')
        except Error as e:
            print(f'Error de actualización de usuario. Detalle: {e.msg}')
        finally:
            connect_validation()
    # DELETE
    def delete_user(self, id):
        sql = f"DELETE FROM user WHERE id_user = '{id}'"
        try:
            connection.cursor.execute(sql)
            connection.db.commit()
            print(f'El usuario con id: {id} fue eliminado')
        except Error as e:
            print(f'Error al eliminar usuario. Detalle: {e.msg}')
        finally:
            connect_validation()

        