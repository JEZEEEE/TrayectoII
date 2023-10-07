import mysql.connector
from bd.basedatos import conexion
from tkinter import messagebox
class Empleado:
    def __init__(self, id_emp, nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp):
        self.id_emp = id_emp
        self.nom_emp = nom_emp
        self.ape_emp = ape_emp
        self.fec_emp_nac = fec_emp_nac
        self.gen_emp = gen_emp
        self.dir_emp = dir_emp
        self.est_emp = est_emp

    @staticmethod
    def crear_empleado(nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp):
        Conexion_clase = conexion()

        if Conexion_clase is not None:
            cursor = Conexion_clase.cursor()

            try:
                query = f"INSERT INTO empleado (nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp) VALUES ('{nom_emp}', '{ape_emp}', '{fec_emp_nac}', '{gen_emp}', '{dir_emp}', '{est_emp}')"
                cursor.execute(query)
                Conexion_clase.commit()

                messagebox.showinfo("Empleado", "Creado Correctamente")
            except mysql.connector.Error as err:
                print(f"Error al crear el empleado: {err}")
                messagebox.showinfo("Empleado", "Error al crear empleado")
                Conexion_clase.rollback()

            finally:
                cursor.close()
                Conexion_clase.close()

        else:
            print("No se pudo conectar a la base de datos.")

    def actualizar_empleado(self):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"UPDATE empleado SET nom_emp = '{self.nom_emp}', ape_emp = '{self.ape_emp}', fec_emp_nac = '{self.fec_emp_nac}', gen_emp = '{self.gen_emp}', dir_emp = '{self.dir_emp}', est_emp = '{self.est_emp}' WHERE id_emp = {self.id_emp}"
            cursor.execute(query)

            Conexion_clase.commit()
            messagebox.showinfo("Empleado", "Actualizado Exitosamente")

        except mysql.connector.Error as err:
            print(f"Error al actualizar el empleado: {err}")
            messagebox.showinfo("Empleado", "Error al Actualizar")
        finally:
            cursor.close()
            Conexion_clase.close()

    @staticmethod
    def eliminar_empleado(id_emp):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"DELETE FROM empleado WHERE id_emp = {id_emp}"
            cursor.execute(query)

            Conexion_clase.commit()
            messagebox.showinfo("Empleado", "Eliminado Exitosamente")

        except mysql.connector.Error as err:
            print(f"Error al eliminar el empleado: {err}")
            messagebox.showwarning("Empleado","No se puede Eliminar al empleado ya que tiene un registro de Asistencia")

        finally:
            cursor.close()
            Conexion_clase.close()

    @staticmethod
    def obtener_empleado_por_id(id_emp):
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"SELECT * FROM empleado WHERE id_emp = {id_emp}"
            cursor.execute(query)

            empleado = cursor.fetchone()

            if empleado:
                return Empleado(*empleado)  # Devuelve una instancia de la clase Empleado con los datos obtenidos
            else:
                print("Empleado no encontrado.")
                return None

        except mysql.connector.Error as err:
            print(f"Error al obtener el empleado: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()

    @staticmethod
    def obtener_todos_los_empleados():
        try:
            Conexion_clase = conexion()
            cursor = Conexion_clase.cursor()

            query = f"SELECT * FROM empleado"
            cursor.execute(query)

            empleados = cursor.fetchall()

            if empleados:
                return [Empleado(*empleado) for empleado in empleados]  # Devuelve una lista de instancias de la clase Empleado
            else:
                print("No se encontraron empleados.")
                return []

        except mysql.connector.Error as err:
            print(f"Error al obtener los empleados: {err}")

        finally:
            cursor.close()
            Conexion_clase.close()
