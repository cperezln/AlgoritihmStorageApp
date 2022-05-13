#Autor##Admin
##BFS
'''

    Breadth First Search is a path-finding algorithm between two nodes in a graph.
    It gets the shortest path if each edge have distance of 1
'''
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
#Autor##Admin
##Dijkstra
'''
    
    Dijkstra's algorithm is an designed to find the shortest paths between nodes in a graph.
    It was designed by a Dutch computer scientist, Edsger Wybe Dijkstra, in 1956, when pondering the shortest route from Rotterdam to Groningen.
    It was published three years later.
'''
def dijkstra(self, start_vertex):
    D = {v: float('inf') for v in range(self.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        self.visited.append(current_vertex)

        for neighbor in range(self.v):
            if self.edges[current_vertex][neighbor] != -1:
                distance = self.edges[current_vertex][neighbor]
                if neighbor not in self.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

#Autor##Juan Antonio
##21 2
##private
'''
aodfbsajkjanb
ghsrbkj�fsj
ts
'''
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
#Autor##Juan Antonio
##Hola mundo 
##public
'''
Acabamos elegir una de las categorias
'''
from appAlgoritmos import Algoritmos
from tkinter import ttk
from tkinter import *
from sqlalchemy import create_engine
if __name__ == '__main__':

    root =Tk() #ventana principal
    app = Algoritmos(root)
    root.mainloop()#Con esto mantenemos la
    # ventana si no se cerraria tras un milisegundo.Esta accion abre un hilo
