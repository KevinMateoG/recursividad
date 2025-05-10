class Graph:
    def __init__(self):
        self.adj_list: dict[int, list[int]] = {}
        self.whigth = 0
        self.size = 0
    
    def add_vertex(self, vertex):
        if vertex in self.adj_list:
            return
        
        self.adj_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2, direct=False, wigth= None):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        
        w = vertex1 if wigth is None else (vertex1, wigth)
        if direct:
            if vertex1 not in self.adj_list[vertex2]:
                self.adj_list[vertex2].append(w)

        w = vertex2 if wigth is None else (vertex2, wigth)
        if vertex2 not in self.adj_list[vertex1]:
            self.adj_list[vertex1].append(w)
    
    def dfs(self, start):
        visitado = []
        recorrido = self.dfs_estructura(start, visitado)
        return recorrido

    def dfs_estructura(self, start, vistado: list):
        if start not in vistado:
            vistado.append(start)
        
        for i in self.adj_list[start]:
            self.dfs_estructura(i, vistado)
        return vistado

    def bfs(self, inicio):
        if inicio not in self.adj_list:
            return
        visitado = []
        por_visitar = [inicio]
        while por_visitar:
            actual = por_visitar.pop(0)
            if actual in visitado:
                continue
            visitado.append(actual)

            por_visitar.extend(self.adj_list[actual])
        return visitado
    
    def verificar_str(self, palabra, formar="", cont = 0, visitado=[], por_visitar=None):
        if por_visitar is None:
            por_visitar = [palabra[0]]
        if palabra[0] not in self.adj_list:
            return False
        
        actual = por_visitar.pop()
        if actual in palabra:
            visitado.append(actual)
            formar += actual
            if formar == palabra:
                return True
            if palabra[cont+1] in self.adj_list[actual]:
                por_visitar.extend(self.adj_list[actual])
            if palabra[cont+1] in por_visitar:
                por_visitar = [palabra[cont+1]]
        cont += 1
        if self.verificar_str(palabra, formar, cont, visitado, por_visitar):
            return True

    def __repr__(self):
        return str(self.adj_list)

g = Graph()
g.add_vertex("h")
g.add_vertex("o")
g.add_vertex("l")
g.add_vertex("a")
g.add_vertex("x")
g.add_vertex("y")
g.add_edge("h", "o")
g.add_edge("h", "y")
g.add_edge("h", "x")
g.add_edge("o", "l")
g.add_edge("o","x")
g.add_edge("x", "h")
g.add_edge("l", "a")
g.add_edge("a", "o")
g.add_edge("a", "l")
print(g)
print(g.verificar_str("hox"))