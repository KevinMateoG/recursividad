class Graph:
    def __init__(self):
        self.size = 0
        self.Nodes: list[int] = []
        self.type: str = None
        self.adj_matrix: list[list[int]] = []
        self.whigth = 0
        self.deafault_whigth = 1
    
    def add_vertex(self, vertex):
        if vertex in self.Nodes:
            return
        self.Nodes.append(vertex)

        for row in self.adj_matrix:
            row.append(0)
        
        self.adj_matrix.append([0] * (self.size+1))
        self.size += 1
    
    def add_edge(self, vertex1, vertex2, direct=False, wigth= None):
        if vertex1 not in self.Nodes:
            self.add_vertex(vertex1)
        
        if vertex2 not in self.Nodes:
            self.add_vertex(vertex2)
        
        pos_vertex1 = self.Nodes.index(vertex1)
        pos_vertex2 = self.Nodes.index(vertex2)
        
        w = self.deafault_whigth if wigth is None else wigth
        if direct:
            self.adj_matrix[pos_vertex2][pos_vertex1] = w
            
        self.adj_matrix[pos_vertex1][pos_vertex2] = w
    
    def dfs(self, start):
        visitado = []
        recorrido = self.dfs_estructura(start, visitado)
        return recorrido

    def dfs_estructura(self, start, vistado: list, cont = 0):
        if start not in vistado:
            vistado.append(start)
        
        for i in self.adj_list[start]:
            self.dfs_estructura(i, vistado)
        return vistado
    def verificar_str(self, palabra):
            ...
    def __repr__(self):
        rep_str = ""
        for i in self.adj_matrix:
            rep_str += str(i) + "\n"
        
        return rep_str

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(4)
g.add_vertex(6)
g.add_vertex(9)
g.add_edge(1,4)
print(g)