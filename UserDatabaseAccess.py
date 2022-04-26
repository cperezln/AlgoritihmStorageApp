from sqlalchemy import create_engine
import re
import hashlib
class UserDatabaseAccess:
    def __init__(self):
        # Aqui declaramos el motor para conectarnos a la base de datos aunque de momento no nos conectamos eso se hará en la función db_consulta
        db = 'sqlite:///database/usuarios.db'
        self.engine = create_engine(db)

#Esta funcion inserta a un nuevo usuario en la base de datos.
    def insertarUsuario(self,param):
        self.validarRegistro(param[0],param[1],param[2])
        query = "INSERT INTO usuarios VALUES( ?,NULL, ?, ?)"
        hash_sha3_224 = hashlib.new("sha3_224", param[1].encode())
        parametros = (param[0], hash_sha3_224.hexdigest(), param[2])
        self.db_consulta(query,parametros)
#Esta y las dos siguientes funciones sirven para comprobar que los parametros del nuevo usuario son correctos/seguros
    def validacion_nombre(self, nom):
        return len(nom) != 0

    def validacion_contrasena(self, contrasena):
        return len(contrasena) >= 10

    def validacion_correo(self, correo):
        return len(correo) > 0, bool(re.match(r"[^@\s]+@[a-zA-z]+(\.[a-zA-Z])+", correo))
#Esta funcion sirve para comprobar que los datoos introducidos para el nuevo usuario son correctos, seguros y no coinciden con los datos de un usuario ya registrado

    def validarRegistro(self, name, password, email):
        query1 = 'SELECT * FROM usuarios WHERE nombre = "{}"'.format(name)
        query2 = 'SELECT * FROM usuarios WHERE correo = "{}"'.format(email)
        aux = self.validacion_correo(email)
        print(self.db_consulta(query2))
        return(aux[0],aux[1],self.validacion_nombre(name),self.validacion_contrasena(password),len(self.db_consulta(query1))==0,len(self.db_consulta(query2))==0)

    def validarAcceso(self,text,con):
        contrasena =  hash_sha3_224 = hashlib.new("sha3_224", con.encode())
        parametros =(text,hash_sha3_224.hexdigest())
        query = 'SELECT nombre,correo FROM usuarios WHERE nombre = "{}" and contrasena ="{}"'.format(parametros[0],parametros[1])
        resul = self.db_consulta(query)
        if(resul == []):
            query = 'SELECT nombre,correo FROM usuarios WHERE correo = "{}" and contrasena ="{}"'.format(parametros[0], parametros[1])
            resul = self.db_consulta(query)
        return ( [resul != [], resul])

    def name(self, email):
        return self.db_consulta('SELECT nombre FROM usuarios WHERE correo = "{}"'.format(email))
    def db_consulta(self, consulta, parametros=()):
        with self.engine.connect() as con:
            # Como aqui obtenemos un puntero, extraeremos los datos y los almacenaremos en una variable
            resultado = []
            try:
                resultado = con.execute(consulta, parametros).fetchall()
            except:
                resultado = []
        return resultado
