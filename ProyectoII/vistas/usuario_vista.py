import tkinter as tk
from tkinter import ttk
from controladores.usuario_controlador import ControladorUsuario

class VistaUsuario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Vista de Usuario")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Vista de Usuario", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.tree_usuarios = ttk.Treeview(self, columns=("ID", "Empleado", "Nombre", "Contraseña", "Rol", "Estatus"))
        self.tree_usuarios.heading("#0", text="ID")
        self.tree_usuarios.heading("#1", text="Empleado")
        self.tree_usuarios.heading("#2", text="Nombre")
        self.tree_usuarios.heading("#3", text="Contraseña")
        self.tree_usuarios.heading("#4", text="Rol")
        self.tree_usuarios.heading("#5", text="Estatus")
        self.tree_usuarios.pack(pady=20)

        self.actualizar_lista_usuarios()

        self.btn_crear_usuario = ttk.Button(self, text="Crear Usuario", command=self.abrir_ventana_crear_usuario)
        self.btn_crear_usuario.pack()

        self.btn_actualizar_usuario = ttk.Button(self, text="Actualizar Usuario", command=self.actualizar_usuario_seleccionado)
        self.btn_actualizar_usuario.pack()

        self.btn_eliminar_usuario = ttk.Button(self, text="Eliminar Usuario", command=self.eliminar_usuario_seleccionado)
        self.btn_eliminar_usuario.pack()

    def actualizar_lista_usuarios(self):
        # Limpiamos los items actuales del Treeview
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)

        # Obtenemos todos los usuarios desde el controlador
        usuarios = ControladorUsuario.obtener_todos_los_usuarios()

        # Agregamos los usuarios al Treeview
        for usuario in usuarios:
            empleado = ControladorUsuario.obtener_empleado_por_id(usuario.id_emp)
            self.tree_usuarios.insert("", "end", text=usuario.id_usu, values=(usuario.id_emp, empleado.nom_emp, usuario.nom_usu, usuario.con_usu, usuario.id_rol, usuario.est_usu))

    def abrir_ventana_crear_usuario(self):
        VentanaCrearUsuario(self)

    def actualizar_usuario_seleccionado(self):
        seleccionado = self.tree_usuarios.focus()
        if seleccionado:
            id_usu = self.tree_usuarios.item(seleccionado, "text")
            usuario = ControladorUsuario.obtener_usuario_por_id(id_usu)
            if usuario:
                VentanaActualizarUsuario(self, usuario)

    def eliminar_usuario_seleccionado(self):
        seleccionado = self.tree_usuarios.focus()
        if seleccionado:
            id_usu = self.tree_usuarios.item(seleccionado, "text")
            ControladorUsuario.eliminar_usuario(id_usu)
            self.actualizar_lista_usuarios()

class VentanaCrearUsuario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Crear Usuario")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Crear Usuario", font=("Arial", 16))
        self.label_titulo.pack(pady=10)


        self.label_id_emp = ttk.Label(self, text="ID Empleado:")
        self.label_id_emp.pack()

        self.entry_id_emp = ttk.Entry(self)
        self.entry_id_emp.pack()


        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.pack()

        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack()

        self.label_contrasena = ttk.Label(self, text="Contraseña:")
        self.label_contrasena.pack()

        self.entry_contrasena = ttk.Entry(self)
        self.entry_contrasena.pack()

        self.label_rol = ttk.Label(self, text="Rol:")
        self.label_rol.pack()

        self.entry_rol = ttk.Entry(self)
        self.entry_rol.pack()

        self.label_estatus = ttk.Label(self, text="Estatus:")
        self.label_estatus.pack()

        self.entry_estatus = ttk.Entry(self)
        self.entry_estatus.pack()

       

        self.btn_guardar = ttk.Button(self, text="Guardar", command=self.crear_usuario)
        self.btn_guardar.pack()

    def crear_usuario(self):
        id_emp = self.entry_id_emp.get()
        nom_usu = self.entry_nombre.get()
        con_usu = self.entry_contrasena.get()
        id_rol = self.entry_rol.get()
        est_usu = self.entry_estatus.get()
        ControladorUsuario.crear_usuario(id_emp, nom_usu, con_usu, id_rol, est_usu)
        self.parent.actualizar_lista_usuarios()
        self.destroy()

class VentanaActualizarUsuario(tk.Toplevel):
    def __init__(self, parent, usuario):
        super().__init__(parent)
        self.parent = parent
        self.usuario = usuario
        self.title("Actualizar Usuario")
        self.geometry("800x600")

        self.label_titulo = ttk.Label(self, text="Actualizar Usuario", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.pack()

        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack()
        self.entry_nombre.insert(0, self.usuario.nom_usu)

        self.label_contrasena = ttk.Label(self, text="Contraseña:")
        self.label_contrasena.pack()

        self.entry_contrasena = ttk.Entry(self)
        self.entry_contrasena.pack()
        self.entry_contrasena.insert(0, self.usuario.con_usu)

        self.label_rol = ttk.Label(self, text="Rol:")
        self.label_rol.pack()

        self.entry_rol = ttk.Entry(self)
        self.entry_rol.pack()
        self.entry_rol.insert(0, self.usuario.id_rol)

        self.label_id_emp = ttk.Label(self, text="ID Empleado:")
        self.label_id_emp.pack()

        self.entry_id_emp = ttk.Entry(self)
        self.entry_id_emp.pack()
        self.entry_id_emp.insert(0, self.usuario.id_emp)

        self.label_estatus = ttk.Label(self, text="Estatus:")
        self.label_estatus.pack()

        self.entry_estatus = ttk.Entry(self)
        self.entry_estatus.pack()
        self.entry_estatus.insert(0, self.usuario.est_usu)

        self.btn_actualizar = ttk.Button(self, text="Actualizar", command=self.actualizar_usuario)
        self.btn_actualizar.pack()

    def actualizar_usuario(self):
        nombre = self.entry_nombre.get()
        contrasena = self.entry_contrasena.get()
        rol = self.entry_rol.get()
        id_emp = self.entry_id_emp.get()
        estatus = self.entry_estatus.get()

        ControladorUsuario.actualizar_usuario(self.usuario.id_usu, nombre, contrasena, id_emp, rol, estatus)
        self.parent.actualizar_lista_usuarios()
        self.destroy()
