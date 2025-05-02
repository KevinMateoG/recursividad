class Graph:
    def __init__(self):
        self.adj_list: dict[int, list[int]] = {}
        self.whigth = 0
        self.size = 0
        self.deafault_whigth = 1
    
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
        self.adj_list[vertex1].append(w)

    def __repr__(self):
        return str(self.adj_list)

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(4)
g.add_vertex(6)
g.add_vertex(9)
g.add_edge(1, 4, True,wigth=10)
print(g)