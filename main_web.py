import UserDatabaseAccess as db
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db = db.UserDatabaseAccess()
@app.route('/')
def main():
    return render_template("login.html", error = "")
@app.route('/login',  methods = ['GET', 'POST'])
def login():
    if[request.method == 'POST']:
        if request.form['action'] == 'login':
            req = request.form
            if(checkAccessDatabase(req.get('email'), req.get('pass'))[0]):
                return redirect(url_for('home'))
            else:
                return render_template("login.html", error = "User not found")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_database', methods = ['GET', 'POST'])
def register_database():
    if [request.method == 'POST']:
        if request.form['action'] == 'register':
            req = request.form
            b1, b2, b3, b4, b5, b6 = db.validarRegistro(req.get('username'), req.get('pass'), req.get('email'))
            if(not b1 or not b2):
                return render_template('register.html', error = "The email is not correct")
            elif(not b3):
                return render_template('register.html', error = "The username is not correct")
            elif(not b4):
                return render_template('register.html', error = "The password is not correct")
            elif(not b5):
                return render_template('register.html', error = "The username is already register")
            elif(not b6):
                return render_template('register.html', error = "The email is already register")
            else:
                db.insertarUsuario([req.get('username'), req.get('pass'), req.get('email')])
                return redirect('/')


@app.route('/index', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/sorting/<algorithm>')
def sorting(algorithm = ""):
    s = []
    with open("codes/Sorting.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#"+algorithm+"\n":
            i+=1
        for j in range(i + 1, len(lines)):
            s.append(lines[j])
    return render_template("render_alg.html", code_list = s)

@app.route('/math/<algorithm>')
def math(algorithm = ""):
    s = []
    with open("codes/Math.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#"+algorithm+"\n":
            i+=1
        for j in range(i + 1, len(lines)):
            s.append(lines[j])
    return render_template("render_alg.html", code_list = s)

@app.route('/dp/<algorithm>')
def dp(algorithm = ""):
    s = []
    with open("codes/Dynammic Programming.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#"+algorithm+"\n":
            i+=1
        for j in range(i + 1, len(lines)):
            s.append(lines[j])
    return render_template("render_alg.html", code_list = s)

@app.route('/graph/<algorithm>')
def graphs(algorithm = ""):
    s = []
    with open("codes/Graph.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#"+algorithm+"\n":
            i+=1
        for j in range(i + 1, len(lines)):
            s.append(lines[j])
    return render_template("render_alg.html", code_list = s)


@app.route('/community/<algorithm>')
def community(algorithm = ""):
    s = []
    with open("codes/Community.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#"+algorithm+"\n":
            i+=1
        for j in range(i + 1, len(lines)):
            s.append(lines[j])
    return render_template("render_alg.html", code_list = s)

def checkAccessDatabase(user, con):
    return db.validarAcceso(user, con)

@app.route('/local')
def login_local():
    content = request.json
    print(content,checkAccessDatabase(content[0], content[1]) )
    return checkAccessDatabase(content[0], content[1])

if __name__ == '__main__':
    app.run(debug=True)
