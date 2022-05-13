import UserDatabaseAccess as db
from flask import Flask, render_template, request, redirect, url_for, Response
import json
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
            if(check_access_database(req.get('email'), req.get('pass'))[0]):
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
    ls = get_community()
    return render_template("index.html", Community = ls)

@app.route('/sorting/<algorithm>')
def sorting(algorithm = ""):
    s = []
    with open("codes/Sorting.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#" + algorithm + "\n":
            i += 1
        for j in range(i + 1, len(lines)):
            if lines[j] != "---\n":
                s.append(lines[j])
            else:
                break
    return render_template("render_alg.html", code_list = s, Community = get_community())

@app.route('/math/<algorithm>')
def math(algorithm = ""):
    s = []
    with open("codes/Math.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#" + algorithm + "\n":
            i += 1
        for j in range(i + 1, len(lines)):
            if lines[j] != "---\n":
                s.append(lines[j])
            else:
                break
    return render_template("render_alg.html", code_list = s, Community = get_community())

@app.route('/dp/<algorithm>')
def dp(algorithm = ""):
    s = []
    with open("codes/Dynammic Programming.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#" + algorithm + "\n":
            i += 1
        for j in range(i + 1, len(lines)):
            if lines[j] != "---\n":
                s.append(lines[j])
            else:
                break
    return render_template("render_alg.html", code_list = s, Community = get_community())

@app.route('/graph/<algorithm>')
def graphs(algorithm = ""):
    s = []
    with open("codes/Graph.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#" + algorithm + "\n":
            i += 1
        for j in range(i + 1, len(lines)):
            if lines[j] != "---\n":
                s.append(lines[j])
            else:
                break
    return render_template("render_alg.html", code_list = s, Community = get_community())


@app.route('/community/<algorithm>')
def community(algorithm = ""):
    s = []
    with open("codes/Community.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#" + algorithm + "\n":
            print(lines[i])
            i+=1
        for j in range(i + 1, len(lines)):
            if lines[j] != "---\n":
                s.append(lines[j])
            else:
                break
    return render_template("render_alg.html", code_list = s, Community = get_community())

@app.route('/local')
def login_local():
    content = request.json
    result = check_access_database(content[0], content[1])

    if( result[0] ):
        return  Response(json.dumps({'b1':result[0], 'res': list(result[1][0])}))
    else:
        return Response(json.dumps({'b1': result[0], 'res': []}))

def check_access_database(user, con):
    return db.validarAcceso(user, con)

def get_community():
    with(open("codes/Community.py")) as f:
        lines = f.readlines()
        res = []
        for i in lines:
            if i.startswith('#'):
                i = i[1::]
                res.append(i)
    return res

@app.route('/upload', methods = ['POST'])
def upload_com():
    content = request.json
    name = content['name']
    user = content['user']
    desc = content['description']
    code = content['content']
    with open('codes/Community.py', "a") as f:
        c = code.split("\n")
        s_code = ""
        for i in c:
            if(not ("#" in i)):
                print(i)
                s_code += i
                s_code += "\n"
        print(s_code)
        new_code = "#{}\n'''\n\tAutor: \t{}\n{}'''\n{}".format(name, user, desc, s_code) + "\n---\n"
        f.write(new_code)
    return Response("")
if __name__ == '__main__':
    app.run(debug=True)
