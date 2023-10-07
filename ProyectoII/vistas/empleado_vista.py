import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controladores.empleado_controlador import ControladorEmpleado
from controladores.asistencia_controlador import ControladorAsistencia
from datetime import date, datetime
import re #Expresiones Regulares para validaciones regexp
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class VistaEmpleado(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Vista de Empleado")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Vista de Empleado", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.tree_empleados = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "Fecha Nacimiento", "Genero", "Direccion", "Estatus"))
        self.tree_empleados.heading("#0", text="ID")
        self.tree_empleados.heading("#1", text="Nombre")
        self.tree_empleados.heading("#2", text="Apellido")
        self.tree_empleados.heading("#3", text="Fecha Nacimiento")
        self.tree_empleados.heading("#4", text="Genero")
        self.tree_empleados.heading("#5", text="Direccion")
        self.tree_empleados.heading("#6", text="Estatus")
        self.tree_empleados.pack(pady=20)

        self.actualizar_lista_empleados()

        
        #BOTONES DE LA VISTA EMPLEADO
        self.btn_crear_empleado = tk.Button(self, text="Crear Empleado", command=self.abrir_ventana_crear_empleado, width=25, height=2, border=7)
        self.btn_crear_empleado.pack()
        self.btn_crear_empleado.place(x=60,y=310)

        self.btn_actualizar_empleado = tk.Button(self, text="Actualizar Empleado", command=self.actualizar_empleado_seleccionado, width=25, height=2, border=7)
        self.btn_actualizar_empleado.pack()
        self.btn_actualizar_empleado.place(x=310,y=310)

        self.btn_eliminar_empleado = tk.Button(self, text="Eliminar Empleado", command=self.eliminar_empleado_seleccionado, width=25, height=2, border=7)
        self.btn_eliminar_empleado.pack()
        self.btn_eliminar_empleado.place(x=530,y=310)

        self.btn_registrar_asistencia = tk.Button(self, text="Registrar Asistencia", command=self.registrar_asistencia, width=25, height=2, border=7)
        self.btn_registrar_asistencia.pack()
        self.btn_registrar_asistencia.place(x=60,y=420)


        self.btn_ver_asistencias = tk.Button(self, text="Ver Asistencias", command=self.ver_asistencias, width=25, height=2, border=7)
        self.btn_ver_asistencias.pack()
        self.btn_ver_asistencias.place(x=530,y=420)

        self.btn_generar_reporte = tk.Button(self, text="Generar Reporte", command=self.generar_reporte_asistencias, width=25, height=2, border=7)
        self.btn_generar_reporte.pack()
        self.btn_generar_reporte.place(x=305,y=420)

    def generar_reporte_asistencias(self):
        print("Generando reporte")
        # Obtener el ID del empleado seleccionado
        seleccionado = self.tree_empleados.focus()
        if seleccionado:
            id_emp = self.tree_empleados.item(seleccionado, "text")

            if id_emp is None or id_emp =="":
                messagebox.showerror("error","Selecciona el empleado antes de genearar el reporte")
        # Obtener todas las asistencias para el empleado desde el controlador de asistencias
        asistencias = ControladorAsistencia().obtener_todas_las_asistencias_por_empleado(id_emp)
        # Obtener todas las asistencias desde el controlador de asistencias
        #asistencias = ControladorAsistencia().obtener_todas_las_asistencias()


        # Nombre del archivo PDF de salida
        nombre_archivo = "reporte_asistencias.pdf"

        # Crear un objeto PDF canvas
        pdf_canvas = canvas.Canvas(nombre_archivo, pagesize=letter)

        # Título del reporte
        pdf_canvas.setFont("Helvetica-Bold", 16)
        pdf_canvas.drawString(100, 750, "Reporte de Asistencias")

        # Encabezados de la tabla
        pdf_canvas.setFont("Helvetica-Bold", 12)
        pdf_canvas.drawString(100, 700, "ID Empleado")
        pdf_canvas.drawString(200, 700, "Fecha")
        pdf_canvas.drawString(300, 700, "Hora Llegada")
        pdf_canvas.drawString(400, 700, "Hora Salida")

        # Contenido de la tabla
        pdf_canvas.setFont("Helvetica", 12)
        y = 680
        for asistencia in asistencias:
            pdf_canvas.drawString(100, y, str(asistencia.id_emp))
            pdf_canvas.drawString(200, y, str(asistencia.fec_asi))
            pdf_canvas.drawString(300, y, str(asistencia.horLle_asi))
            pdf_canvas.drawString(400, y, str(asistencia.horSal_asi))
            y -= 20

        # Guardar el documento PDF
        pdf_canvas.save()

        print(f"El reporte se ha generado en el archivo {nombre_archivo}")
        messagebox.showinfo("Creado","Reporte Generado {nombre_archivo}")


    def actualizar_lista_empleados(self):
        # Limpiamos los items actuales del Treeview
        for item in self.tree_empleados.get_children():
            self.tree_empleados.delete(item)

        # Obtenemos todos los empleados desde el controlador
        empleados = ControladorEmpleado().obtener_todos_los_empleados()

        # Agregamos los empleados al Treeview
        for empleado in empleados:
            self.tree_empleados.insert("", "end", text=empleado.id_emp, values=(empleado.nom_emp, empleado.ape_emp, empleado.fec_emp_nac, empleado.gen_emp, empleado.dir_emp, empleado.est_emp))

    def abrir_ventana_crear_empleado(self):
        VentanaCrearEmpleado(self)

    def actualizar_empleado_seleccionado(self):
        seleccionado = self.tree_empleados.focus()
        if seleccionado:
            id_emp = self.tree_empleados.item(seleccionado, "text")
            empleado = ControladorEmpleado().obtener_empleado_por_id(id_emp)
            if empleado:
                VentanaActualizarEmpleado(self, empleado)

    def eliminar_empleado_seleccionado(self):
        seleccionado = self.tree_empleados.focus()
        if seleccionado:
            id_emp = self.tree_empleados.item(seleccionado, "text")
            ControladorEmpleado().eliminar_empleado(id_emp)
            self.actualizar_lista_empleados()
            
    def registrar_asistencia(self):
        seleccionado = self.tree_empleados.focus()
        if seleccionado:
            id_emp = self.tree_empleados.item(seleccionado, "text")
            fecha_actual = date.today()
            hora_actual = datetime.now().strftime("%H:%M:%S")
            ControladorAsistencia.registrar_asistencia(id_emp, fecha_actual, hora_actual, "00:00:00")
            self.actualizar_lista_empleados()
    

    def ver_asistencias(self):
        VentanaAsistencias(self)

class VentanaAsistencias(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Ver Asistencias")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Asistencias de Empleados", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.tree_asistencias = ttk.Treeview(self, columns=("ID Asistencia", "ID Empleado", "ID Departamento", "Fecha Asistencia", "Hora Llegada", "Hora Salida"))
        self.tree_asistencias.heading("#0", text="ID Asistencia")
        self.tree_asistencias.heading("#1", text="ID Empleado")
        self.tree_asistencias.heading("#2", text="ID Departamento")
        self.tree_asistencias.heading("#3", text="Fecha Asistencia")
        self.tree_asistencias.heading("#4", text="Hora Llegada")
        self.tree_asistencias.heading("#5", text="Hora Salida")
        self.tree_asistencias.pack(pady=20)

        self.actualizar_lista_asistencias()

        self.btn_cerrar = tk.Button(self, text="Cerrar", command=self.destroy, width=25, height=2, border=7)
        self.btn_cerrar.pack(pady=10)
        self.btn_cerrar.place(x=120,y=310)

        self.btn_registrar_salida = tk.Button(self, text="Registrar Salida", command=self.registrar_salida,width=25, height=2, border=7)
        self.btn_registrar_salida.pack()
        self.btn_registrar_salida.place(x=340,y=310)


    
    def actualizar_lista_asistencias(self):
        asistencias = ControladorAsistencia.obtener_todas_las_asistencias()
        for asistencia in asistencias:
            self.tree_asistencias.insert("", "end", text=asistencia.id_asi, values=(asistencia.id_emp, asistencia.id_dep, asistencia.fec_asi, asistencia.horLle_asi, asistencia.horSal_asi))

    def registrar_salida(self):
        seleccionado = self.tree_asistencias.focus()
        if seleccionado:
            id_asi = self.tree_asistencias.item(seleccionado, "text")
            ControladorAsistencia.registrar_hora_salida(id_asi)
            self.actualizar_lista_asistencias()
                
class VentanaCrearEmpleado(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Crear Empleado")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Crear Empleado", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.pack()

        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack()

        self.label_apellido = ttk.Label(self, text="Apellido:")
        self.label_apellido.pack()

        self.entry_apellido = ttk.Entry(self)
        self.entry_apellido.pack()

        self.label_fecha_nacimiento = ttk.Label(self, text="Fecha Nacimiento:")
        self.label_fecha_nacimiento.pack()

        self.entry_fecha_nacimiento = ttk.Entry(self)
        self.entry_fecha_nacimiento.pack()

        self.label_genero = ttk.Label(self, text="Género:")
        self.label_genero.pack()

        self.combo_genero = ttk.Combobox(self, values=["Masculino", "Femenino"])
        self.combo_genero.pack()

        self.label_direccion = ttk.Label(self, text="Dirección:")
        self.label_direccion.pack()

        self.entry_direccion = ttk.Entry(self)
        self.entry_direccion.pack()

        self.label_estatus = ttk.Label(self, text="Estatus:")
        self.label_estatus.pack()

        self.combo_estatus = ttk.Combobox(self, values=["Activo", "Inactivo"])
        self.combo_estatus.pack()

        self.btn_crear_empleado = tk.Button(self, text="Crear Empleado", command=self.crear_empleado, width=25, height=2, border=7)
        self.btn_crear_empleado.pack()

    def crear_empleado(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        genero = self.combo_genero.get()
        direccion = self.entry_direccion.get()
        estatus = self.combo_estatus.get()

       # Creamos una lista para almacenar los campos faltantes
        campos_faltantes = []

        # Validamos que se hayan ingresado todos los campos
        if not nombre:
            campos_faltantes.append("Nombre")

        if not apellido:
            campos_faltantes.append("Apellido")

        if not fecha_nacimiento:
            campos_faltantes.append("Fecha de nacimiento")

        if not genero:
            campos_faltantes.append("Género")

        if not direccion:
            campos_faltantes.append("Dirección")

        if not estatus:
            campos_faltantes.append("Estatus")

        # Validamos el nombre y apellido utilizando expresiones regulares
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            campos_faltantes.append("Nombre válido")

        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", apellido):
            campos_faltantes.append("Apellido válido")

        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
            if fecha_nacimiento >= date.today():
                messagebox.showerror("Error", "La fecha de nacimiento debe ser anterior a la fecha actual.")
                return

        except ValueError:
            messagebox.showerror("Error", "Fecha de nacimiento inválida. Por favor, utiliza el formato AÑO-MES-DIA.")
            return

        # Si hay campos faltantes, mostramos un mensaje de error con todas las opciones faltantes
        if campos_faltantes:
            mensaje_error = "Por favor, completa los siguientes campos: " + ", ".join(campos_faltantes)
            messagebox.showerror("Error", mensaje_error)
            return
        
        # Creamos el empleado a través del controlador
        ControladorEmpleado().crear_empleado(nombre, apellido, fecha_nacimiento, genero, direccion, estatus)

        # Actualizamos la lista de empleados en la vista principal
        self.parent.actualizar_lista_empleados()

        # Cerramos la ventana de crear empleado
        self.destroy()

class VentanaActualizarEmpleado(tk.Toplevel):
    def __init__(self, parent, empleado):
        super().__init__(parent)
        self.parent = parent
        self.empleado = empleado
        self.title("Actualizar Empleado")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Actualizar Empleado", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.pack()

        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack()
        self.entry_nombre.insert(0, self.empleado.nom_emp)

        self.label_apellido = ttk.Label(self, text="Apellido:")
        self.label_apellido.pack()

        self.entry_apellido = ttk.Entry(self)
        self.entry_apellido.pack()
        self.entry_apellido.insert(0, self.empleado.ape_emp)

        self.label_fecha_nacimiento = ttk.Label(self, text="Fecha Nacimiento:")
        self.label_fecha_nacimiento.pack()

        self.entry_fecha_nacimiento = ttk.Entry(self)
        self.entry_fecha_nacimiento.pack()
        self.entry_fecha_nacimiento.insert(0, self.empleado.fec_emp_nac)

        self.label_genero = ttk.Label(self, text="Género:")
        self.label_genero.pack()

        self.combo_genero = ttk.Combobox(self, values=["Masculino", "Femenino"])
        self.combo_genero.pack()
        self.combo_genero.set(self.empleado.gen_emp)

        self.label_direccion = ttk.Label(self, text="Dirección:")
        self.label_direccion.pack()

        self.entry_direccion = ttk.Entry(self)
        self.entry_direccion.pack()
        self.entry_direccion.insert(0, self.empleado.dir_emp)

        self.label_estatus = ttk.Label(self, text="Estatus:")
        self.label_estatus.pack()

        self.combo_estatus = ttk.Combobox(self, values=["Activo", "Inactivo"])
        self.combo_estatus.pack()
        self.combo_estatus.set(self.empleado.est_emp)

        self.btn_actualizar_empleado = tk.Button(self, text="Actualizar Empleado", command=self.actualizar_empleado, width=25, height=2, border=7)
        self.btn_actualizar_empleado.pack()

    def actualizar_empleado(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        genero = self.combo_genero.get()
        direccion = self.entry_direccion.get()
        estatus = self.combo_estatus.get()

       
        # Creamos una lista para almacenar los campos faltantes
        campos_faltantes = []

        # Validamos que se hayan ingresado todos los campos
        if not nombre:
            campos_faltantes.append("Nombre")

        if not apellido:
            campos_faltantes.append("Apellido")

        if not fecha_nacimiento:
            campos_faltantes.append("Fecha de nacimiento")

        if not genero:
            campos_faltantes.append("Género")

        if not direccion:
            campos_faltantes.append("Dirección")

        if not estatus:
            campos_faltantes.append("Estatus")

        # Validamos el nombre y apellido utilizando expresiones regulares
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            campos_faltantes.append("Nombre válido")

        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", apellido):
            campos_faltantes.append("Apellido válido")

        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
            if fecha_nacimiento >= date.today():
                messagebox.showerror("Error", "La fecha de nacimiento debe ser anterior a la fecha actual.")
                return

        except ValueError:
            messagebox.showerror("Error", "Fecha de nacimiento inválida. Por favor, utiliza el formato AÑO-MES-DIA.")
            return

        # Si hay campos faltantes, mostramos un mensaje de error con todas las opciones faltantes
        if campos_faltantes:
            mensaje_error = "Por favor, completa los siguientes campos: " + ", ".join(campos_faltantes)
            messagebox.showerror("Error", mensaje_error)
            return
        
         # Validamos que se hayan ingresado todos los campos
        if nombre and apellido and fecha_nacimiento and genero and direccion and estatus:
            # Actualizamos el empleado a través del controlador
            ControladorEmpleado().actualizar_empleado(self.empleado.id_emp, nombre, apellido, fecha_nacimiento, genero, direccion, estatus)

         # Actualizamos la lista de empleados en la vista principal
        self.parent.actualizar_lista_empleados()

            # Cerramos la ventana de actualizar empleado
        self.destroy()

    