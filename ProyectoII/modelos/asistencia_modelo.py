import mysql.connector
from bd.basedatos import conexion
from tkinter import messagebox

class Asistencia:
    def __init__(self, id_asi, id_emp, id_dep, fec_asi, horLle_asi, horSal_asi):
        self.id_asi = id_asi
        self.id_emp = id_emp
        self.id_dep = id_dep
        self.fec_asi = fec_asi
        self.horLle_asi = horLle_asi
        self.horSal_asi = horSal_asi

    def registrar_asistencia(id_emp, fecha, hora_llegada, hora_salida):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"INSERT INTO asistencia (id_emp, fec_asi, horLle_asi, horSal_asi) VALUES ({id_emp}, '{fecha}', '{hora_llegada}', '{hora_salida}')"
            cursor.execute(query)

            Conexion_clase.commit()
            print("Asistencia registrada exitosamente!")
            messagebox.showinfo("Asistencia", "Asistencia Registrada Exitosamente")

        except mysql.connector.Error as err:
            print(f"Error al registrar la asistencia: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()
    def obtener_todas_las_asistencias():
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = "SELECT * FROM asistencia"
            cursor.execute(query)

            asistencias = []

            for (id_asi, id_emp, id_dep, fec_asi, horLle_asi, horSal_asi) in cursor:
                asistencia = Asistencia(id_asi, id_emp, id_dep, fec_asi, horLle_asi, horSal_asi)
                asistencias.append(asistencia)

            return asistencias

        except mysql.connector.Error as err:
            print(f"Error al obtener las asistencias: {err}")
            return []

        finally:
            cursor.close()
            Conexion_clase.close()
    def registrar_hora_salida(id_asi, hora_salida):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            # Actualizamos la hora de salida de la asistencia
            query = f"UPDATE asistencia SET horSal_asi = '{hora_salida}' WHERE id_asi = {id_asi}"
            cursor.execute(query)
            Conexion_clase.commit()
            print("Hora de salida registrada exitosamente!")
            messagebox.showinfo("Registro Exitoso", "Hora de salida registrada exitosamente")

        except mysql.connector.Error as err:
            print(f"Error al registrar la hora de salida: {err}")
            messagebox.showerror("Error", "Ocurrió un error al registrar la hora de salida")

        finally:
            cursor.close()
            Conexion_clase.close()

    @classmethod
    def obtener_por_id(self, id_asi):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"SELECT * FROM asistencia WHERE id_asi = {id_asi}"
            cursor.execute(query)

            asistencia = None

            for (id_asi, id_emp, id_dep, fec_asi, horLle_asi, horSal_asi) in cursor:
                asistencia = Asistencia(id_asi, id_emp, id_dep, fec_asi, horLle_asi, horSal_asi)

            return asistencia

        except mysql.connector.Error as err:
            print(f"Error al obtener la asistencia: {err}")
            return None

        finally:
            cursor.close()
            Conexion_clase.close()
    #Cambios para generar el pdf
    @staticmethod
    def obtener_todas_las_asistencias_por_empleado(id_emp):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()
        
            # Consulta SQL para obtener las asistencias para el empleado con el ID proporcionado.
            query = f"SELECT * FROM asistencia WHERE id_emp = '{id_emp}'"
            cursor.execute(query)
            registros = cursor.fetchall()

            # Creamos una lista para almacenar los objetos Asistencia
            asistencias = []

            for registro in registros:
                asistencia = Asistencia(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                asistencias.append(asistencia)
            
            Conexion_clase.close()  # Cerrar la conexión a la base de datos
            return asistencias

        except Exception as e:
            print("Error al obtener las asistencias del empleado:", str(e))
            messagebox.showwarning("Error","Error al obtener las asistencia del empleado")
            return []
