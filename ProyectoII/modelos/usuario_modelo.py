from bd.basedatos import conexion
import mysql.connector

class Usuario:
    def __init__(self, id_usu, id_emp, nom_usu, con_usu, id_rol, est_usu):
        self.id_usu = id_usu
        self.id_emp = id_emp
        self.nom_usu = nom_usu
        self.con_usu = con_usu
        self.id_rol = id_rol
        self.est_usu = est_usu

    def crear_usuario(self, id_emp, nom_usu, con_usu, id_rol, est_usu):
        Conexion_clase = conexion()

        if Conexion_clase is not None:
            cursor = Conexion_clase.cursor()

            try:
                query = f"INSERT INTO usuario (id_emp, nom_usu, con_usu, id_rol, est_usu) VALUES ('{id_emp}, '{nom_usu}, '{con_usu}, '{id_rol}, '{est_usu})"
                cursor.execute(query)
                Conexion_clase.commit()

                print("Usuario creado exitosamente.")

            except mysql.connector.Error as err:
                print(f"Error al crear el usuario: {err}")
                Conexion_clase.rollback()

            finally:
                cursor.close()
                Conexion_clase.close()

        else:
            print("No se pudo conectar a la base de datos.")

    def actualizar_usuario(self, id_usu, id_emp, nom_usu, con_usu, id_rol, est_usu):
        # Método para actualizar los datos de un usuario existente en la base de datos
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"UPDATE usuario SET id_emp = '{id_emp}', nom_usu = '{nom_usu}', con_usu = '{con_usu}', id_rol = '{id_rol}', est_usu = '{est_usu}' WHERE id_usu = '{id_usu}'"
            cursor.execute(query)

            Conexion_clase.commit()
            print("Usuario actualizado exitosamente!")

        except mysql.connector.Error as err:
            print(f"Error al actualizar el usuario: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()

    def eliminar_usuario(self, id_usu):
        # Método para eliminar un usuario de la base de datos por su ID de usuario
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"DELETE FROM usuario WHERE id_usu = '{id_usu}'"
            cursor.execute(query)

            Conexion_clase.commit()
            print("Usuario eliminado exitosamente!")

        except mysql.connector.Error as err:
            print(f"Error al eliminar el usuario: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()

    def obtener_usuario_por_id(self, id_usu):
        # Método para obtener un usuario de la base de datos por su ID de usuario
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"SELECT * FROM usuario WHERE id_usu = '{id_usu}'"
            cursor.execute(query)

            usuario = cursor.fetchone()

            if usuario:
                return self(*usuario)  # Devuelve una instancia de la clase Usuario con los datos obtenidos
            else:
                print("Usuario no encontrado.")
                return None

        except mysql.connector.Error as err:
            print(f"Error al obtener el usuario: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()

    def obtener_todos_los_usuarios(self):
        # Método para obtener todos los usuarios de la base de datos
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"SELECT * FROM usuario"
            cursor.execute(query)

            usuarios = cursor.fetchall()

            if usuarios:
                return [self(*usuario) for usuario in usuarios]  # Devuelve una lista de instancias de la clase Usuario
            else:
                print("No se encontraron usuarios.")
                return []

        except mysql.connector.Error as err:
            print(f"Error al obtener los usuarios: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()
    def obtener_usuario(self, nom_usu):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"SELECT * FROM usuario WHERE nom_usu = '{nom_usu}'"
            print(query)
            cursor.execute(query)

            usuario = cursor.fetchone()

            if usuario:
                # Devuelve una instancia de la clase Usuario con los datos obtenidos
                return Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5])
            else:
                print("Usuario no encontrado.")
                return None

        except mysql.connector.Error as err:
            print(f"Error al obtener el usuario: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()
    