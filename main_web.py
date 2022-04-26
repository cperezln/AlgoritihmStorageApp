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
            if(checkAccessDatabase(req.get('email'), req.get('pass'))[0]):
                return redirect('/index')
            else:
                return render_template("login.html", error = "User not found")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    pass
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
    result =checkAccessDatabase(content[0], content[1])
    print(result )
    return  Response(json.dumps({'b1':result[0], 'res': list(result[1][0])}))

if __name__ == '__main__':
    app.run(debug=True)
