import mysql.connector

def conexion():
    # Configuración de la conexión a la base de datos
    configuracion = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'asistencia', 
        'port': 3306
    }

    try:
        connection = mysql.connector.connect(**configuracion)
        return connection

    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")
        return None
