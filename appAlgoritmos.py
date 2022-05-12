import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import re

from UserDatabaseAccess import UserDatabaseAccess
import requests
class Algoritmos:
    actUser =[]
    SavedAlg = []
    def __init__(self, root):

        #variable que se usará para las consultas a la base de datos de los usuarios
        self.dbConsults = UserDatabaseAccess()
        self.window = root  # Almacenamos la ventana
        self.window.wm_iconbitmap('recursos/AppIcon.ico')
        self.window.title("Register")
        #Creamos el Labelframe sobre el que introduciremos los elementos para registrar usuarios e iniciar sesion
        self.frame = LabelFrame(self.window, text="register", font=('Calibri', 16, 'bold'))
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))

        #Finalmente ejecutamos la función que inicializará la pantalla para crear nuevos usuarios
        self.logIn()


    def logIn(self):
       #Como esta configuración se alterna con la de signUp,cambiaremos el nombre del frame y borraremos los elementos que pueda contener
        self.frame.configure(text="LogIn")
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.grid(row=0, column=0, columnspan=5, pady=20, rowspan=3, padx=10)

        # Fila del nombre del usuario a logear
        name_label = Label(self.frame, text="Name: ", font=('Calibri', 13))
        name_label.grid(row=1, column=0)
        self.name = Entry(self.frame, font=('Calibri', 13))
        self.name.grid(row=1, column=1, columnspan=5)
        self.name.focus()

        # Fila de la contraseña del usuario a logear
        password_label = Label(self.frame, text="Password: ", font=('Calibri', 13))
        password_label.grid(row=2, column=0)
        self.password = Entry(self.frame, font=('Calibri', 13), show='*')
        self.password.grid(row=2, column=1, columnspan=5)

        # Boton para altenar con la pantalla de registro de nuevo usuario

        #Boton para confirmar los datos introducidos

        login_bttn = ttk.Button(self.frame, text="Confirmar", command=self.InicioSesion, style='my.TButton')
        login_bttn.grid(row=3, column=3, columnspan=3)

       #Compartimento en el que se indicara si el usuario con la contraseña introducido se encuntra en la base de datos

        self.message = Label(self.frame,text="", fg='red')
        self.message.grid(row=4, column=0, columnspan=6, sticky=W + E)

    def InicioSesion(self):
        self.message['text']=''
        try:
            r1=requests.get('http://127.0.0.1:5000/local',json=[self.name.get(),self.password.get()])
            if r1.ok:
                r = r1.json()
            else:
                self.message['text'] ='Wrong user or password'
        except:
            self.message['text'] ='Service unable, try again later'
            return
        if (r["b1"]):
            self.actUser = r['res'][0]
            for widget in self.frame.winfo_children():
                widget.destroy()
            delattr(self, "name")
            delattr(self, "password")
            try:
                delattr(self, "mail")
            except( Exception ):
                pass

            self.Acceso()
        else:
            self.message['text']='Wrong user or password'


    def retriveAlg(self,bttn_name):
        for row in self.contentTable.get_children():
            self.contentTable.delete(row)
        if bttn_name != "":
            with  open('codes/{}-local.py'.format(bttn_name), 'r') as e:
                i =0
                alg =e.read()
                alg = alg.split("#Autor")[1:]

                for string in alg :
                    aux = string.split("##")

                    if (self.actUser == aux[1].replace('\n','')  ):
                        aux2 = aux[3].split("'''")
                        self.contentTable.insert('', 0,iid =i ,values=(aux[2].replace("\n",""),aux[1].replace("\n",""), aux2[0].replace("\n","")))
                        i+=1
                        self.SavedAlg.append([aux[2].replace("\n",""),aux2[1],aux2[2]])

                    if ("Admin" == aux[1].replace('\n','')):

                        aux2 = aux[2].split("'''")
                        self.contentTable.insert('', 0,iid =i,  values=(aux2[0].replace("\n",""),aux[1].replace("\n",""), "public"))
                        i += 1
                        self.SavedAlg.append([aux2[0].replace("\n",""),aux2[1], aux2[2]])

        else:
            #Creo que esto no es necesari pero he decidido dejarlo por si acaso
            self.message['text'] ="Select a category"

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
        self.message2 = Label(frame_add,text="", fg='red')
        self.message2.grid(row =8,column = 0, columnspan =3, sticky = E+W)

    def storeAlg(self):
        self.message2["text"]=""
        alg_name = self.alg_name.get("1.0",END).replace("\r","").replace("\n"," ")
        if (len(alg_name) < 2):
            self.message2["text"] += "Add a name "
        if (not (self.rad_value.get() == 1 or self.rad_value.get() == 2)):
            self.message2["text"] += " select a visibility option "
        if (filename == ""):
            self.message2["text"] += " select a .py file"
        if (len(self.category_bttn.get())==0):
            self.message2["text"] += " select a category"
        if filename != "" and len(alg_name) != 0 and (self.rad_value.get()==1 or self.rad_value.get()==2) and len(self.category_bttn.get())>0:

            self.storeFile(filename, alg_name,self.rad_value.get(),self.description.get("1.0",END),self.category_bttn.get())

            self.window_add.grab_release()
            self.window_add.destroy()
            delattr(self,"window_add")
            delattr(self, "message2")
            delattr(self, "confirm_bttn")
            delattr(self, "description")
            delattr(self, "rad_value")
            delattr(self, "alg_name")
            delattr(self, "image")
            delattr(self, "category_bttn")
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

    def storeFile(self,file,alg_name,visibility, des,cat):

        if visibility == 1:
            try:
                with open(file, "r") as e2:
                    r =requests.post('http://127.0.0.1:5000/upload', json={"name": alg_name, "user": self.actUser,
                                                                       "description": des,
                                                                     "content": e2.read()})
                    self.message['text'] = "Algorithm added successfully"
                    if not r.ok:
                        self.message['text'] = 'There was an error adding the algorithm'
                    else:
                        try:
                            with  open('codes/{}-local.py'.format(cat), 'a') as e:
                                e.write("#Autor##" + self.actUser + "\n")
                                e.write("##" + alg_name + "\n")
                                if (visibility == 1):
                                    e.write("##public\n")
                                else:
                                    e.write("##private\n")
                                e.write("'''\n{}'''\n".format(des))
                                with open(file, "r") as e2:
                                    e.write(e2.read())
                            self.message['text'] = "Algorithm added successfully"
                        except:
                            self.message['text'] = "There was an error adding the algorithm"
            except:
                self.message['text'] = 'There was an error adding the algorithm'
        else:
            try:
                with  open('codes/{}-local.py'.format(cat),'a') as e:
                    e.write("#Autor##"+self.actUser+"\n")
                    e.write("##"+alg_name+"\n")
                    if (visibility ==1):
                        e.write("##public\n")
                    else:
                        e.write("##private\n")
                    e.write("'''\n{}'''\n".format(des))
                    with open(file,"r") as e2:
                        e.write(e2.read())
                self.message['text'] = "Algorithm added successfully"
            except:
                self.message['text'] = "There was an error adding the algorithm"



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

        self.window.title("Algorithm App")
        self.frame.configure(text="Algoritmos")
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame.grid(row=0, column=0, columnspan=6, pady=20, rowspan=14, padx=10)
        self.message =Label(self.frame, text="", fg='red')
        self.message.grid(row =13, column =1, columnspan = 9)
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
        self.sunkenButtn = self.mathsButn
        self.cuadroParaTabla = Frame(self.frame,height =13)
        #Esto no se porque es pero si pongo row 1 la tabla se me baja más de la cuenta
        self.cuadroParaTabla.grid(row =0, rowspan = 13, columnspan = 4)
        self.contentTable = ttk.Treeview(self.cuadroParaTabla, columns = ("name","autor","visibility"),show='headings')
        self.contentTable.grid(row =0, rowspan =13,columnspan=4)
        self.contentTable.heading('name', text ='Name')
        self.contentTable.heading('autor', text='Author')
        self.contentTable.heading('visibility', text='Visibility')
        self.contentTable.pack(side = LEFT)
        self.contentTable.bind("<1>", self.OnClick)
        self.scrollBarY = Scrollbar(self.cuadroParaTabla, orient=VERTICAL,command=self.contentTable.yview)
        self.scrollBarY.pack(side=RIGHT, fill=Y)

        self.contentTable.config(yscrollcommand=self.scrollBarY.set )
        #Frame que nos permitirá mostrar los algoritmos

        self.showAlg = LabelFrame(self.frame,text ="",font=('times new roman',16,'bold'))
        self.showAlg.grid(row =0, rowspan = 12, column =4 )
        self.Alg = Text(self.showAlg,state =DISABLED,width=40,height=20,wrap =NONE)


        self.scrollBarAlgY = Scrollbar(self.showAlg, orient=VERTICAL,command=self.Alg.yview)
        self.scrollBarAlgY.pack(side=RIGHT, fill=Y)
        self.scrollBarAlgX =Scrollbar(self.showAlg, orient=HORIZONTAL,command=self.Alg.xview)
        self.scrollBarAlgX.pack(side =BOTTOM,fill =X)
        self.Alg.pack()
        self.Alg.config(yscrollcommand=self.scrollBarAlgY.set,xscrollcommand =self.scrollBarAlgX.set)
        self.retriveAlg(self.sunkenButtn['text'])
        self.addButtn = Button(self.frame, text = "Add",command =self.addAlg)
        self.addButtn.grid(row =11, column =0,columnspan=4,sticky = E+W)
