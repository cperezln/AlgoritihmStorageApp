import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import re
import hashlib
from UserDatabaseAccess import UserDatabaseAccess
import requests
class Algoritmos:
    usuarioAct =[]
    SavedAlg = []
    def __init__(self, root):

        #variable que se usará para las consultas a la base de datos de los usuarios
        self.dbConsults = UserDatabaseAccess()
        self.ventana = root  # Almacenamos la ventana
        self.ventana.wm_iconbitmap('recursos/AppIcon.ico')
        self.ventana.title("Register")
        #Creamos el Labelframe sobre el que introduciremos los elementos para registrar usuarios e iniciar sesion
        self.frame = LabelFrame(self.ventana, text="register", font=('Calibri', 16, 'bold'))
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))

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

        self.mensaje = Label(self.frame,text="", fg='red')
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

        self.mensaje = Label(self.frame,text="", fg='red')
        self.mensaje.grid(row=4, column=0, columnspan=6, sticky=W + E)
    #Función que registra al usuario si todos los campos están rellenos y ni el nombre ni el correo coincide con ningún usuario ya registrado
    def registrarse(self):
        self.mensaje['text']=''
        #Hacemos la consulta a nuestro controlador de la base de datos
        b1, b2,b3, b4,b5,b6 = self.dbConsults.validarRegistro(self.nombre.get(),self.contrasena.get(),self.correo.get())
        self.mensaje['text'] = ""
        #Si el controlador nos devuelve alguno de los boolenos negativos, entonces alguo de los campos es incorrecto y lo indicamos en
        #el elemento de los errores
        if (b1 and b2 and b3 and b4 and not b5 and b6):
            self.dbConsults.insertarUsuario((self.nombre.get(),self.contrasena.get(),self.correo.get()))
            self.InicioSesion()
        if (not b3):
            self.mensaje['text'] += "El nombre es obligatorio\n"
        if( b5):
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
        r1=requests.post('http://127.0.0.1:8080',json=[self.nombre.get(),self.contrasena.get()])

        if (r1):
            self.usuarioAct = r2[0][0]

            for widget in self.frame.winfo_children():
                widget.destroy()
            delattr(self, "nombre")
            delattr(self, "contrasena")
            try:
                delattr(self, "correo")
            except( Exception ):
                pass

            self.Acceso()
        else:
            self.mensaje['text']='Usuario o contraseña incorrectos'


    def retriveAlg(self,bttn_name):
        print(bttn_name)
        for fila in self.contentTable.get_children():
            self.contentTable.delete(fila)
        if bttn_name != "Community" and bttn_name !="":
            with  open('codes/{}-local.py'.format(bttn_name), 'r') as e:
                i =0
                alg =e.read()
                alg = alg.split("#Autor")[1:]

                for string in alg :
                    aux = string.split("##")

                    if (self.usuarioAct == aux[1].replace('\n','')  ):
                        aux2 = aux[3].split("'''")
                        print(aux2)
                        self.contentTable.insert('', 0,iid =i ,values=(aux[2].replace("\n",""),aux[1].replace("\n",""), aux2[0].replace("\n","")))
                        i+=1
                        self.SavedAlg.append([aux[2].replace("\n",""),aux2[1],aux2[2]])
                        #self.contentTable.insert(id,0,text=aux2[1])
                        #self.contentTable.insert(id, 1,text=aux2[2])
                    if ("Admin" == aux[1].replace('\n','')):

                        aux2 = aux[2].split("'''")
                        self.contentTable.insert('', 0,iid =i,  values=(aux2[0].replace("\n",""),aux[1].replace("\n",""), "public"))
                        i += 1
                        self.SavedAlg.append([aux2[0].replace("\n",""),aux2[1], aux2[2]])

        else:
            pass




    filename =''
    def addAlg(self):
        global filename
        filename =''
        def browseFiles(label_file_explorer):
            global filename
            filenameaux= filedialog.askopenfilename(initialdir="/",
                                                  title="Select a File",
                                                  filetypes=(("Python files",
                                                              "*.py*"),))
            if (filenameaux != ""):
                file = re.findall('/[^/]+\.py',filenameaux)[0]
                label_file_explorer.configure(text="File Opened: "+file )
                filename = filenameaux




        #Creación del popup para añadir nuevos algoritnos
        self.window_add = Toplevel()
        self.window_add.grab_set()
        self.window_add.title = "Add Algorithm"
        self.window_add.resizable(1,1)
        self.window_add.wm_iconbitmap('recursos/AppIcon.ico')



        #Contenedor de los elementos de la ventana
        frame_add = LabelFrame(self.window_add,text ="Add Algorithm",font=('times new roman',16,'bold'))
        frame_add.grid(row=0, column=0, columnspan=3, pady=20)
        # Fila nuevo nombre
        alg_name_label = Label(frame_add, text=" Name : ", font=('Calibri', 20))
        alg_name_label.grid(row=1, column=0,sticky=E+W+N+S)
        self.alg_name = Text(frame_add, font=('Calibri', 13),height=1,width =50)
        self.alg_name.grid(row=1, column=1)
        public_private_container = LabelFrame(frame_add,text ="Visibility")
        public_private_container.grid(row=1, column =2)
        self.rad_value =tkinter.IntVar()
        rad_bttn1= tkinter.Radiobutton(public_private_container,text = 'public',variable = self.rad_value,value =1)
        rad_bttn1.pack(side= TOP)
        rad_bttn2 = tkinter.Radiobutton(public_private_container, text='private', variable=self.rad_value, value=2)
        rad_bttn2.pack(side=BOTTOM)
        # Filas para la descripcion
        description_label = Label(frame_add, text="Description:", font=('Calibri', 13))
        description_label.grid(row=2, column=0, columnspan = 3)
        self.description = Text(frame_add, font=('Calibri', 13),height=4)
        self.description.grid(row=3, column=0,columnspan=3,sticky= E+W)

        # Fila seleccion dxe programa de momento solo admite .py
        program_file_label = Label(frame_add, text="Programn:", font=('Calibri', 13))
        program_file_label.grid(row=5, column=0,columnspan =2,sticky=W)
        self.image = PhotoImage(file='recursos/folder.png')


        programn_select_bttn = Button(frame_add,image=self.image,command = lambda :browseFiles(program_file_label))
        programn_select_bttn.grid(row=5, column=2)

        #Fila seleccion categoria
        category_label = Label(frame_add, text="Category:", font=('Calibri', 13))
        category_label.grid(row =6, column=0)
        self.category_bttn = ttk.Combobox(frame_add,state="readonly",values=["Math", "Sorting", "Graph", "Dynammic Programming"])
        self.category_bttn.grid(row =6, column =1, columnspan = 2)
        #Boton para confimar
        self.confirm_bttn = Button(frame_add, text="Confirm",command =self.storeAlg)
        self.confirm_bttn.grid(row =7,column = 0,columnspan =3 ,sticky=E+W)
        self.mensaje2 = Label(frame_add,text="", fg='red')
        self.mensaje2.grid(row =8,column = 0, columnspan =3, sticky = E+W)

    def storeAlg(self):
        self.mensaje2["text"]=""
        alg_name = self.alg_name.get("1.0",END).replace("\r","").replace("\n"," ")
        if (len(alg_name) < 2):
            self.mensaje2["text"] += "Add a name "
        if (not (self.rad_value.get() == 1 or self.rad_value.get() == 2)):
            self.mensaje2["text"] += " select a visibility option "
        if (filename == ""):
            self.mensaje2["text"] += " select a .py file"
        if (len(self.category_bttn.get())==0):
            self.mensaje2["text"] += " select a category"
        if filename != "" and len(alg_name) != 0 and (self.rad_value.get()==1 or self.rad_value.get()==2) and len(self.category_bttn.get())>0:

            self.storeFile(filename, alg_name,self.rad_value.get(),self.description.get("1.0",END),self.category_bttn.get())
            self.mensaje['text'] = "Algorith added successfully"
            self.window_add.grab_release()
            self.window_add.destroy()
            delattr(self,"window_add")
            delattr(self, "mensaje2")
            delattr(self, "confirm_bttn")
            delattr(self, "description")
            delattr(self, "rad_value")
            delattr(self, "alg_name")
            delattr(self, "image")
            delattr(self, "category_bttn")
            print(self.__dict__)
            self.SavedAlg = []
            self.retriveAlg(self.sunkenButtn['text'])
    def OnClick(self,event):
        item = self.contentTable.identify('item', event.x, event.y)

        if (item):
            self.showAlg['text'] = self.SavedAlg[int(item)][0]
            self.Alg.configure(state='normal')
            self.Alg.delete('1.0', END)
            self.Alg.insert('1.0',self.SavedAlg[int(item)][1]+self.SavedAlg[int(item)][2])
            self.Alg.configure(state='disabled')
            print("you clicked on",item )

    def storeFile(self,file,alg_name,visibility, des,cat):
        with  open('codes/{}-local.py'.format(cat),'a') as e:
            e.write("#Autor##"+self.usuarioAct+"\n")
            e.write("##"+alg_name+"\n")
            if (visibility ==1):
                e.write("##public\n")
            else:
                e.write("##private\n")
            e.write("'''\n{}'''\n".format(des))
            with open(file,"r") as e2:
                e.write(e2.read())
        if visibility == 1:
            pass

    def DeleteAlg(self):
        pass
    def Acceso(self):
        # Esta función lo que hará es que la pestaña de categoría seleccionada se quede selecionada
        #y se deseleccione la anterior

        def leavePressed( button):

            if (self.sunkenButtn != None):
                self.sunkenButtn.configure(relief="raised")
            self.SavedAlg = []
            if(button != self.sunkenButtn):
                button.configure(relief="sunken")
                self.sunkenButtn = button
                self.retriveAlg(self.sunkenButtn['text'])
            else:
                self.sunkenButtn.configure(relief="raised")
                self.sunkenButtn = None
                self.retriveAlg('')

        self.ventana.title("Algorithm App")
        self.frame.configure(text="Algoritmos")
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame.grid(row=0, column=0, columnspan=6, pady=20, rowspan=14, padx=10)
        self.mensaje =Label(self.frame, text="", fg='red')
        self.mensaje.grid(row =13, column =1, columnspan = 9)
        self.mathsButn = Button(self.frame, text = "Math")
        self.mathsButn.configure(command = lambda:leavePressed(self.mathsButn),relief="sunken")
        self.mathsButn.grid(row=0, column=0,sticky = E+W)
        self.sortButn = Button(self.frame, text="Sorting")
        self.sortButn.configure( command= lambda:leavePressed(self.sortButn))
        self.sortButn.grid(row=0, column=1,sticky = E+W)
        self.GraphButn = Button(self.frame, text="Graph")
        self.GraphButn.configure(command=lambda:leavePressed(self.GraphButn))
        self.GraphButn.grid(row=0, column=2,sticky = E+W)
        self.DynamicButn = Button(self.frame, text="Dynammic Programming" )
        self.DynamicButn.configure(command=lambda:leavePressed(self.DynamicButn))
        self.DynamicButn.grid(row=0, column=3,sticky = E+W)
        self.CommunityButn = Button(self.frame, text="Community")
        self.CommunityButn.configure(command=lambda:leavePressed(self.CommunityButn))
        self.sunkenButtn = self.mathsButn
        self.CommunityButn.grid(row=0, column=4,sticky = E+W)
        self.cuadroParaTabla = Frame(self.frame,height =13)
        self.cuadroParaTabla.grid(row =1, rowspan = 13, columnspan = 5)
        self.contentTable = ttk.Treeview(self.cuadroParaTabla, columns = ("nombre","autor","visibility"),show='headings')
        self.contentTable.grid(row =1, rowspan =13,columnspan=5)
        self.contentTable.heading('nombre', text ='Name')
        self.contentTable.heading('autor', text='Author')
        self.contentTable.heading('visibility', text='Visibility')
        self.contentTable.pack(side = LEFT)
        self.contentTable.bind("<1>", self.OnClick)
        self.scrollBarY = Scrollbar(self.cuadroParaTabla, orient=VERTICAL,command=self.contentTable.yview)
        self.scrollBarY.pack(side=RIGHT, fill=Y)

        self.contentTable.config(yscrollcommand=self.scrollBarY.set )
        #Frame que nos permitirá mostrar los algoritmos

        self.showAlg = LabelFrame(self.frame,text ="",font=('times new roman',16,'bold'))
        self.showAlg.grid(row =0, rowspan = 13, column =5 )
        self.Alg = Text(self.showAlg,state =DISABLED,width=40,height=20,wrap =NONE)


        self.scrollBarAlgY = Scrollbar(self.showAlg, orient=VERTICAL,command=self.Alg.yview)
        self.scrollBarAlgY.pack(side=RIGHT, fill=Y)
        self.scrollBarAlgX =Scrollbar(self.showAlg, orient=HORIZONTAL,command=self.Alg.xview)
        self.scrollBarAlgX.pack(side =BOTTOM,fill =X)
        self.Alg.pack()
        self.Alg.config(yscrollcommand=self.scrollBarAlgY.set,xscrollcommand =self.scrollBarAlgX.set)
        self.retriveAlg(self.sunkenButtn['text'])
        self.addButtn = Button(self.frame, text = "Add",command =self.addAlg)
        self.addButtn.grid(row =12, column =0,columnspan=3,sticky = E+W)
        self.deleteBttn = Button(self.frame, text = "Delete",command=self.DeleteAlg)
        self.deleteBttn.grid(row =12, column =3,columnspan=2,sticky = E+W)