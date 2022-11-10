"""Este archivo esta creado como un totorial básico para establecer una conexión con la BBDD.
Nota: Installar el modulo mysql-connector-python para evitar el error: Authentication plugin 'caching_sha2_password'
Para ello ejecutar en consola: pip install mysql-connector-python"""

import mysql.connector
from mysql.connector import Error

# PASOS A SEGUIR PARA CONECTAR BBDD

try:
    # 1- Abrir-Crear Conexión
    # aca van las variables que informan los datos de la conexión a MySql
    connection = mysql.connector.connect(
        user = 'root', #usuario MySql
        password = 'root', #password MySql
        host = 'localhost', #Servidor
        database = 'capacit', #Base de datos
        port = '3306',) #puerto de MySql por defecto
    
    # 2- Crear cursor. 
    cursor = connection.cursor() #Este es un objeto que sirve para ejecutar las consultas.
    
    # 3- Ejecutar consulta sql
    cursor.execute("SELECT DATABASE();")  
    # En el cursor se guardan los datos de la consulta
    # (en este caso pedimos que muestre la base de datos pero puede ser cualquier consulta sql)
    
    # 4- Manejar los resultados de la consulta
    result = cursor.fetchone()
    # para poder ver los datos guardados en el cursor hay que extraerlos en una variable. 
    # fetchone si es un solo resultado. (Una sola fila de tabla)
    # Fetchall sin son multiples resultados. (2 o más filas de una tabla)
    # Nota: Si quisieramos hacer una operación de Create, Delete o Update, entonces
    # luego de la instruccion cursor.execute("query") se debe agregar connection.commit() para confirmar la ejecución.
    # No así para una operación Read.   
    
    print(f"Se estableció la conexión con la base de datos {result}")
except Error as e:
    print(f"Error al conectar la base de datos: {e.msg}") #Hacemos manejo de cualquier error que pueda surgir en la conexión
finally:
    if connection.is_connected():  # si se realizó la conexión...
# 5- Cerrar puntero
        cursor.close()
# 6- Cerrar conexión
        connection.close()
        #Los pasos 5 y 6 se deben ejecutar siempre que se finalice una consulta a la BBDD para evitar errores.
        print("La conexión de Mysql fue cerrada")
