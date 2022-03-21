from tkinter import ttk
from tkinter import *
import re
import hashlib
from UserDatabaseAccess import UserDtabaseAccess

class Algoritmos:
    usuarioAct =[]
    def __init__(self, root):
        #variable que se usará para las consultas a la base de datos de los usuarios
        self.dbConsults = UserDtabaseAccess()
        self.ventana = root  # Almacenamos la ventana
        self.ventana.wm_iconbitmap('recursos/AppIcon.ico')
        self.ventana.title("Inicio de sesión")
        #Creamos el Labelframe sobre el que introduciremos los elementos para registrar usuarios e iniciar sesion
        self.frame = LabelFrame(self.ventana, text="Registrarse", font=('Calibri', 16, 'bold'))
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.nombre =[]
        self.contrasena =[]
        self.correo =[]
        #Finalmente ejecutamos la función que inicializará la pantalla para crear nuevos usuarios
        self.SignUp()

    #Función que genera los elementos de la pantalla en la que un nuevo usuario se registra
    def SignUp(self):
        # Como la pantalla de registro se alterna con la de login, primero eliminamos todos los elementos del Labelframe
        for widget in self.frame.winfo_children():
            widget.destroy()
        #Y cambiamos las características del marco para que se ajusten a su uso actual
        self.frame.configure(text="Registrarse")
        self.frame.grid(row=0, column=0, columnspan=5, pady=20, rowspan=4, padx=10)

        # Fila del nombre del nuevo usuario
        etiqueta_nombre = Label(self.frame, text="Nombre: ", font=('Calibri', 13))
        etiqueta_nombre.grid(row=1, column=0)
        self.nombre = Entry(self.frame, font=('Calibri', 13))
        self.nombre.grid(row=1, column=1, columnspan=5)
        self.nombre.focus()

        # Fila la contraseña del nuevo usuario
        etiqueta_contrasena = Label(self.frame, text="Contraseña: ", font=('Calibri', 13))
        etiqueta_contrasena.grid(row=2, column=0)
        self.contrasena = Entry(self.frame, font=('Calibri', 13), show='*')
        self.contrasena.grid(row=2, column=1, columnspan=5)

        # Fila del correo del nuevo usuario
        etiqueta_correo = Label(self.frame, text="Correo: ", font=('Calibri', 13))
        etiqueta_correo.grid(row=3, column=0)
        self.correo = Entry(self.frame, font=('Calibri', 13))
        self.correo.grid(row=3, column=1, columnspan=5)

        # Boton para cambiar  al pantalla de registro

        boton_signin = ttk.Button(self.frame, text="Iniciar sesion", command=self.logIn, style='my.TButton')
        boton_signin.grid(row=4, column=0, columnspan=3)

        #Boton para registrarse tras introducir los datos

        boton_signup = ttk.Button(self.frame, text="Confirmar", command=self.registrarse, style='my.TButton')
        boton_signup.grid(row=4, column=3, columnspan=3)

        #Zona donde se mostrarán los errores en los datos introducidos

        self.mensaje = Label(text="", fg='red')
        self.mensaje.grid(row=5, column=0, columnspan=6, sticky=W + E)

    #función que inicializa los elementos del Labelframe para el login de los usuarios
    def logIn(self):
       #Como esta configuración se alterna con la de signUp,cambiaremos el nombre del frame y borraremos los elementos que pueda contener
        self.frame.configure(text="LogIn")
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.grid(row=0, column=0, columnspan=5, pady=20, rowspan=3, padx=10)

        # Fila del nombre del usuario a logear
        etiqueta_nombre = Label(self.frame, text="Nombre: ", font=('Calibri', 13))
        etiqueta_nombre.grid(row=1, column=0)
        self.nombre = Entry(self.frame, font=('Calibri', 13))
        self.nombre.grid(row=1, column=1, columnspan=5)
        self.nombre.focus()

        # Fila de la contraseña del usuario a logear
        etiqueta_contrasena = Label(self.frame, text="Contraseña: ", font=('Calibri', 13))
        etiqueta_contrasena.grid(row=2, column=0)
        self.contrasena = Entry(self.frame, font=('Calibri', 13), show='*')
        self.contrasena.grid(row=2, column=1, columnspan=5)

        # Boton para altenar con la pantalla de registro de nuevo usuario

        boton_signup = ttk.Button(self.frame, text="No tengo Cuenta", command=self.SignUp, style='my.TButton')
        boton_signup.grid(row=3, column=0, columnspan=3)

        #Boton para confirmar los datos introducidos

        boton_login = ttk.Button(self.frame, text="Confirmar", command=self.InicioSesion, style='my.TButton')
        boton_login.grid(row=3, column=3, columnspan=3)

       #Compartimento en el que se indicara si el usuario con la contraseña introducido se encuntra en la base de datos

        self.mensaje = Label(text="", fg='red')
        self.mensaje.grid(row=4, column=0, columnspan=6, sticky=W + E)
    #Función que registra al usuario si todos los campos están rellenos y ni el nombre ni el correo coincide con ningún usuario ya registrado
    def registrarse(self):
        self.mensaje['text']=''
        #Hacemos la consulta a nuestro controlador de la base de datos
        b1, b2,b3, b4,b5,b6 = self.dbConsults.validarRegistro(self.nombre.get(),self.contrasena.get(),self.correo.get())
        self.mensaje['text'] = ""
        #Si el controlador nos devuelve alguno de los boolenos negativos, entonces alguo de los campos es incorrecto y lo indicamos en
        #el elemento de los errores
        if (not b3):
            self.mensaje['text'] += "El nombre es obligatorio\n"
        if(not b5):
            self.mensaje['text'] += "El nombre introducido ya pertenece a un usuario\n"
        if (not b4):
            self.mensaje['text'] += "La contraseña  debe tener un tamaño superior a los 9 caracteres\n"
        if (not b1):
            self.mensaje['text'] += "El correo es obligatorio\n"
        if (not b6):
            self.mensaje['text'] += "El correo introducido ya pertenece a otro usuario\n"
        if (not b2):
            self.mensaje['text'] += "El formato del correo debe ser:\n 'cadena de texto'@'dominios seguidos de punto salvo el último'"
    #Función que comprueba que el usuario esta registrado he inicia sesión con dicho usuario si es el caso
    def InicioSesion(self):
        self.mensaje['text']=''
        r1,r2 =self.dbConsults.validarAcceso(self.nombre.get(),self.contrasena.get())
        if (r1):
            self.usuarioAct = r2[0][0]
            self.mensaje['text'] = 'Usuario y contraseña contraseña correctos.\nBienvenido: {}'.format(self.usuarioAct)
        else:
            self.mensaje['text']='Usuario o contraseña incorrectos'
