from modelos.empleado_modelo import Empleado

class ControladorEmpleado:

    def crear_empleado(self, nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp):
        Empleado.crear_empleado(nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp)

    def actualizar_empleado(self, id_emp, nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp):
        empleado = Empleado(id_emp, nom_emp, ape_emp, fec_emp_nac, gen_emp, dir_emp, est_emp)
        empleado.actualizar_empleado()

    def eliminar_empleado(self, id_emp):
        Empleado.eliminar_empleado(id_emp)

    def obtener_empleado_por_id(self, id_emp):
        return Empleado.obtener_empleado_por_id(id_emp)

    def obtener_todos_los_empleados(self):
        return Empleado.obtener_todos_los_empleados()
