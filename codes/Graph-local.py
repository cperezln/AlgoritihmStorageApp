#Author:Juan Antonio
#21 2
#private
"""
aodfbsajkjanb
ghsrbkj�fsj
ts
"""
import UserDatabaseAccess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/index')
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


if __name__ == '__main__':
    app.run(debug=True)
