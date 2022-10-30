"""Este archivo esta creado como un totorial básico para establecer una conexión con la BBDD.
Nota: Installar el modulo mysql-connector-python para evitar el error: Authentication plugin 'caching_sha2_password'
Para ello ejecutar en consola: pip install mysql-connector-python"""

import mysql.connector
from mysql.connector import Error

# PASOS A SEGUIR PARA CONECTAR BBDD

try:
    # 1- Abrir-Crear Conexión
    # aca van las variables que informan los datos de la conexión
    connection = mysql.connector.connect(
        user = 'root', 
        password = 'root', 
        host = 'localhost', 
        database = 'capacit', 
        port = '3306',)
    
    # 2- Crear cursor. Este es un objeto que sirve para ejecutar las consultas.
    cursor = connection.cursor()
    
    # 3- Ejecutar consulta sql
    # En el cursor se guardan los datos de la consulta
    cursor.execute("select database();")
    
    # 4- Manejar los resultados de la consulta
    # para poder ver los datos guardados en el cursor hay que extraerlos en una variable. 
    # fetchone si es un solo resultado. 
    # Fetchall sin son multiples resultados.
    # Nota: Si lo que se desea es hacer una operación de Create, Delete o Update luego de la instruccion cursor.execute("Consulta sql")
    # se debe agregar connection.commit() para confirmar la ejecución. No así para una operación Read.   
    result = cursor.fetchone()
    print(f"Se estableció la conexión con la base de datos {result}")
except Error as e:
    print(f"Error al conectar la base de datos: {e.msg}")
finally:
    # si se realizó la conexión cerrar puntero y conexión. Esta instrucción se debe ejecutar siempre que se finalice una consulta a la BBDD.
    if connection.is_connected():
# 5- Cerrar puntero
        cursor.close()
# 6- Cerrar conexión
        connection.close()
        print("La conexión de Mysql fue cerrada")
