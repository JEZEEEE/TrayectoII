from modelos.usuario_modelo import Usuario
import mysql.connector
from bd.basedatos import conexion

class ControladorUsuario:

    def crear_usuario(self, id_emp, nom_usu, con_usu, id_rol, est_usu):
        usuario = Usuario(None, id_emp, nom_usu, con_usu, id_rol, est_usu)
        usuario.crear_usuario()

    def actualizar_usuario(self, id_usu, id_emp, nom_usu, con_usu, id_rol, est_usu):
        usuario = Usuario(id_usu, id_emp, nom_usu, con_usu, id_rol, est_usu)
        usuario.actualizar_usuario()

    def eliminar_usuario(self, id_usu):
        usuario = Usuario(id_usu, None, None, None, None, None)
        usuario.eliminar_usuario()

    def obtener_usuario_por_id(self, id_usu):
        usuario = Usuario(id_usu, None, None, None, None, None)
        return usuario.obtener_usuario_por_id(id_usu)

    def obtener_todos_los_usuarios(self):
        usuario = Usuario(None, None, None, None, None, None)
        return usuario.obtener_todos_los_usuarios()
    
    def obtener_usuario_por_nombre(self, nom_usu):
        connection = conexion()

        if connection is not None:
            cursor = connection.cursor()

            try:
                query = f"SELECT * FROM usuario WHERE nom_usu = '{nom_usu}'"
                cursor.execute(query)
                print(query)

                usuario = cursor.fetchone()

                if usuario:
                    print(usuario)
                    return Usuario(*usuario)  # Devuelve una instancia de la clase Usuario con los datos obtenidos
                else:
                    print("Usuario no encontrado.")
                    return None

            except mysql.connector.Error as err:
                print(f"Error al obtener el usuario: {err}")

            finally:
                cursor.close()
                connection.close()

        else:
            print("No se pudo conectar a la base de datos.")
            return None
