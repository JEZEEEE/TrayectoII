from modelos.asistencia_modelo import Asistencia
from bd.basedatos import conexion
import mysql.connector
from datetime import date, datetime
from tkinter import messagebox
class ControladorAsistencia:
    def registrar_asistencia(id_emp, fecha, hora_llegada, hora_salida):
        Asistencia.registrar_asistencia(id_emp, fecha, hora_llegada, hora_salida)
  
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
    def registrar_hora_salida(id_asi):
        # Obtener la hora actual
        hora_salida = datetime.now().strftime("%H:%M:%S")

        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            # Realizar la consulta UPDATE para actualizar la hora de salida
            query = f"UPDATE asistencia SET horSal_asi = '{hora_salida}' WHERE id_asi = {id_asi}"
            cursor.execute(query)

            Conexion_clase.commit()
            print("Hora de salida registrada exitosamente!")
            messagebox.showinfo("Hora de Salida", "Hora de salida registrada exitosamente!")
        except mysql.connector.Error as err:
            print(f"Error al registrar la hora de salida: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()
    #cambios para generar el pdf
    @staticmethod
    def obtener_todas_las_asistencias_por_empleado(id_emp):
        print(id_emp)
        return Asistencia.obtener_todas_las_asistencias_por_empleado(id_emp)