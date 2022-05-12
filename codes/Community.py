



#Hello World
'''
    Autor: Admin
    A hello world program
'''

def hello_world():
    print("Hello World!")

---
#ireogbdsa<skfhvk
'''
	Autor: 	Juan Antonio
hgobz�whfbd �ifgx
'''
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

        self.dbConsults = UserDatabaseAccess()
        self.ventana.wm_iconbitmap('recursos/AppIcon.ico')
        self.ventana.title("Register")
        self.frame = LabelFrame(self.ventana, text="register", font=('Calibri', 16, 'bold'))
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))

        self.logIn()


    def logIn(self):
        self.frame.configure(text="LogIn")
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.grid(row=0, column=0, columnspan=5, pady=20, rowspan=3, padx=10)

        etiqueta_nombre = Label(self.frame, text="Nombre: ", font=('Calibri', 13))
        etiqueta_nombre.grid(row=1, column=0)
        self.nombre = Entry(self.frame, font=('Calibri', 13))
        self.nombre.grid(row=1, column=1, columnspan=5)
        self.nombre.focus()

        etiqueta_contrasena = Label(self.frame, text="Contraseña: ", font=('Calibri', 13))
        etiqueta_contrasena.grid(row=2, column=0)
        self.contrasena = Entry(self.frame, font=('Calibri', 13), show='*')
        self.contrasena.grid(row=2, column=1, columnspan=5)



        boton_login = ttk.Button(self.frame, text="Confirmar", command=self.InicioSesion, style='my.TButton')
        boton_login.grid(row=3, column=3, columnspan=3)


        self.mensaje = Label(self.frame,text="", fg='red')
        self.mensaje.grid(row=4, column=0, columnspan=6, sticky=W + E)

    def InicioSesion(self):
        self.mensaje['text']=''
        try:
            r1=requests.get('http://127.0.0.1:5000/local',json=[self.nombre.get(),self.contrasena.get()])
            if r1.ok:
                r = r1.json()
            else:
                self.mensaje['text'] ='Usuario o contraseña incorrectos'


        except:
            self.mensaje['text'] ='Servicio no disponible, intentelo más tarde'
            return
        print(r)
        if (r["b1"]):
            self.usuarioAct = r['res'][0]
            print(self.usuarioAct)
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
        if bttn_name !="":
            with  open('codes/{}-local.py'.format(bttn_name), 'r') as e:
                i =0
                alg =e.read()

                for string in alg :

                    if (self.usuarioAct == aux[1].replace('\n','')  ):
                        aux2 = aux[3].split("'''")
                        print(aux2)
                        self.contentTable.insert('', 0,iid =i ,values=(aux[2].replace("\n",""),aux[1].replace("\n",""), aux2[0].replace("\n","")))
                        i+=1
                        self.SavedAlg.append([aux[2].replace("\n",""),aux2[1],aux2[2]])
                    if ("Admin" == aux[1].replace('\n','')):

                        aux2 = aux[2].split("'''")
                        self.contentTable.insert('', 0,iid =i,  values=(aux2[0].replace("\n",""),aux[1].replace("\n",""), "public"))
                        i += 1
                        self.SavedAlg.append([aux2[0].replace("\n",""),aux2[1], aux2[2]])

        else:
            self.mensaje['text'] ="Select a category"




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




        self.window_add = Toplevel()
        self.window_add.grab_set()
        self.window_add.title = "Add Algorithm"
        self.window_add.resizable(1,1)
        self.window_add.wm_iconbitmap('recursos/AppIcon.ico')



        frame_add = LabelFrame(self.window_add,text ="Add Algorithm",font=('times new roman',16,'bold'))
        frame_add.grid(row=0, column=0, columnspan=3, pady=20)
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
        description_label = Label(frame_add, text="Description:", font=('Calibri', 13))
        description_label.grid(row=2, column=0, columnspan = 3)
        self.description = Text(frame_add, font=('Calibri', 13),height=4)
        self.description.grid(row=3, column=0,columnspan=3,sticky= E+W)

        program_file_label = Label(frame_add, text="Programn:", font=('Calibri', 13))
        program_file_label.grid(row=5, column=0,columnspan =2,sticky=W)
        self.image = PhotoImage(file='recursos/folder.png')


        programn_select_bttn = Button(frame_add,image=self.image,command = lambda :browseFiles(program_file_label))
        programn_select_bttn.grid(row=5, column=2)

        category_label = Label(frame_add, text="Category:", font=('Calibri', 13))
        category_label.grid(row =6, column=0)
        self.category_bttn = ttk.Combobox(frame_add,state="readonly",values=["Math", "Sorting", "Graph", "Dynammic Programming"])
        self.category_bttn.grid(row =6, column =1, columnspan = 2)
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

        if visibility == 1:
            try:
                with open(file, "r") as e2:
                    r =requests.post('http://127.0.0.1:5000/upload', json={"name": alg_name, "user": self.usuarioAct,
                                                                       "description": des,
                                                                     "content": e2.read()})
                    self.mensaje['text'] = "Algorithm added successfully"
                    if not r.ok:
                        self.mensaje['text'] = 'There was an error adding the algorithm'
                    else:
                        try:
                            with  open('codes/{}-local.py'.format(cat), 'a') as e:
                                if (visibility == 1):
                                else:
                                e.write("'''\n{}'''\n".format(des))
                                with open(file, "r") as e2:
                                    e.write(e2.read())
                            self.mensaje['text'] = "Algorithm added successfully"
                        except:
                            self.mensaje['text'] = "There was an error adding the algorithm"
            except:
                self.mensaje['text'] = 'There was an error adding the algorithm'
        else:
            try:
                with  open('codes/{}-local.py'.format(cat),'a') as e:
                    if (visibility ==1):
                    else:
                    e.write("'''\n{}'''\n".format(des))
                    with open(file,"r") as e2:
                        e.write(e2.read())
                self.mensaje['text'] = "Algorithm added successfully"
            except:
                self.mensaje['text'] = "There was an error adding the algorithm"



    def Acceso(self):

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
        self.sunkenButtn = self.mathsButn
        self.cuadroParaTabla = Frame(self.frame,height =13)
        self.cuadroParaTabla.grid(row =0, rowspan = 13, columnspan = 4)
        self.contentTable = ttk.Treeview(self.cuadroParaTabla, columns = ("nombre","autor","visibility"),show='headings')
        self.contentTable.grid(row =0, rowspan =13,columnspan=4)
        self.contentTable.heading('nombre', text ='Name')
        self.contentTable.heading('autor', text='Author')
        self.contentTable.heading('visibility', text='Visibility')
        self.contentTable.pack(side = LEFT)
        self.contentTable.bind("<1>", self.OnClick)
        self.scrollBarY = Scrollbar(self.cuadroParaTabla, orient=VERTICAL,command=self.contentTable.yview)
        self.scrollBarY.pack(side=RIGHT, fill=Y)

        self.contentTable.config(yscrollcommand=self.scrollBarY.set )

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


---

