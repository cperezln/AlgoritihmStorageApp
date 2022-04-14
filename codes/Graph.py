#BFS
'''
    Autor: Admin
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
#Dijkstra
'''
    Autor: Admin
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
