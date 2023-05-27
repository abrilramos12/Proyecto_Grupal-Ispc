from Entitys.User import User #Importamos la clase User
from Dao.UserDao import UserDao #Importamos la clase UserDao

""" ejemplo de usuario a insertar (este se debería crear en el servicio)
    Nota importante: El id debe ser distinto cada vez que se crea un nuevo usuario no esta definido como autoincremental """
#           id_user /first_name/last_name/ username/        email              /password/active/ role  /create_time/user_git/user_linkedin
user1 = User('1',   'Nicolás', 'Ramos', 'jnramos','jnicolas.ramos10@gmail.com','1234',    '1' , 'ADMIN',  None,   'null',    'null')

user_dao = UserDao()

""" descomentar la siguiente linea para llamar al metodo guardar usuario """
# user_dao.save_user(user1)

""" descomentar la siguiente linea para llamar al metodo buscar usuario """
# print(user_dao.find_user(user1.id_user))

''' Descomentar la siguiente linea para modificar el username del usuario.
    La variable new_username tiene el valor que se quiere actualizar en el atributo username de user1'''
# new_username = 'Nikachin'
# user_dao.update_username(user1.id_user, new_username)

'''descomentar la siguiente linea para borrar usuario'''
# user_dao.delete_user(user1.id_user)



