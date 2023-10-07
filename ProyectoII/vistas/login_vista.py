import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Importamos el módulo messagebox
from controladores.usuario_controlador import ControladorUsuario
from vistas.usuario_vista import VentanaCrearUsuario, VistaUsuario
from vistas.empleado_vista import VistaEmpleado
from PIL import Image, ImageTk

class VistaLogin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Login del Sitema")
        self.geometry("500x400")

        #imagen_fondo = Image.open("Imagenes/fondo.png")
        #imagen_fondo = imagen_fondo.resize((500, 400))
        #imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

        #self.label_fondo = ttk.Label(self, image= imagen_fondo)
        #self.label_fondo.image = imagen_fondo  
        #self.label_fondo.pack()


        self.label_titulo = tk.Label(self, text="Login del Sistema", font=("Arial", 22))
        self.label_titulo.pack(pady=10)

        self.label_usuario = tk.Label(self, text="Usuario:", font=("Arial", 16) )
        self.label_usuario.pack()
        self.label_usuario.place(x=105, y=70)

        self.entry_usuario = tk.Entry(self,width=25, borderwidth=2)
        self.entry_usuario.pack()
        self.entry_usuario.place(x=200, y=75)

        self.label_contrasena = tk.Label(self, text="Contraseña:", font=("Arial", 16))
        self.label_contrasena.pack()
        self.label_contrasena.place(x= 70, y=120)

        self.entry_contrasena = tk.Entry(self, show="*",width=25,borderwidth=2)
        self.entry_contrasena.pack()
        self.entry_contrasena.place(x=200, y=125)


        self.btn_login = tk.Button(self, text="Iniciar Sesion", command=self.login, height=2, width=20)
        self.btn_login.pack()
        self.btn_login.place(x=200, y=190)

    #    self.btn_registrar = ttk.Button(self, text="Registrar Usuario", command=self.abrir_ventana_registrar_usuario)
     #   self.btn_registrar.pack()

    def abrir_ventana_registrar_usuario(self):
                VentanaCrearUsuario(self)  
    def login(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")
        if self.verificar_credenciales(usuario, contrasena):
            self.parent.mostrar_vista_empleado()  # Nueva función para mostrar la vista de empleados
            self.destroy()
            messagebox.showinfo("Inicio de Sesion", "Credenciales Correctas")
        else:
            # Credenciales inválidas, mostramos una alerta
            messagebox.showerror("Error de inicio de sesión", "Credenciales inválidas. Por favor, verifica tu usuario y contraseña.")

    def mostrar_vista_empleado(self):
        self.vista_empleado = VistaEmpleado(self)

    def verificar_credenciales(self, usuario, contrasena):
       # Llamamos al controlador de usuario para obtener los datos del usuario
        usuario_encontrado = ControladorUsuario().obtener_usuario_por_nombre(usuario)



        if usuario_encontrado and usuario_encontrado.con_usu == contrasena:
            # Si el usuario es encontrado y la contraseña coincide, devuelve True
            return True
        else:
            # Si el usuario no es encontrado o la contraseña no coincide, devuelve False
            return False


if __name__ == "__main__":
    app = VistaLogin(None)  # Aquí, "None" es el parent (no tiene parent)
    app.mainloop()
