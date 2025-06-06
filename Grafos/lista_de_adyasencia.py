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

    def dfs_estructura(self, start, vistado: list=[]):
        if start not in vistado:
            vistado.append(start)
        
        for i in self.adj_list[start]:
            if i not in vistado:
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

    def verificar_str(self, palabra, formar = "", vertex = None, cont=0):
        if palabra[cont] not in self.adj_list:
            return False
        if vertex is None:
            vertex = palabra[cont]
        
        for node in self.adj_list:
            if node == vertex:
                formar += vertex
                if formar == palabra:
                        return True
                for nodes in self.adj_list[node]:
                    if nodes == palabra[cont+1]:
                        if self.verificar_str(palabra, formar, nodes, cont+1):
                            return True
        return False

    
    def verificar_ciclos(self, value, visitado: list=[], padre=None):
        visitado.append(value)
        for vecino in self.adj_list[value]:
            if vecino not in visitado:
                if self.verificar_ciclos(vecino, visitado, value):
                    return True
            if vecino == padre:
                return True
        return False
    
    def contar_ciclos(self, value, visitado: list=[], padre=None, cont = 0):
        visitado.append(value)
        for vecino in self.adj_list[value]:
            if vecino not in visitado:
                if self.verificar_ciclos(vecino, visitado, value, cont+1)[0]:
                    return (True, cont+1)
            
            if vecino == padre:
                return (True, cont+1)
        return (False, cont)
    
    def tiene_ciclo(self):
        for vertice in self.adj_list:
            if self.verificar_ciclos(vertice):
                
                return True
    
    def grado_nodo(self, nodo_elegido, cont=0, entrad=True):
        if nodo_elegido not in self.adj_list:
            return 
        if entrad is True:
            for nodo in self.adj_list:
                if nodo_elegido in self.adj_list[nodo]:
                    cont+=1
            return cont
        else:
            return len(self.adj_list[nodo_elegido])

    def eliminar_nodo(self, nodo_eliminar):
        if nodo_eliminar not in self.adj_list:
            return 
        self.adj_list.pop(nodo_eliminar)
        for node in self.adj_list:
            if nodo_eliminar in self.adj_list[node]:
                self.adj_list[node].remove(nodo_eliminar)
        
        return self.adj_list
    
    def primer_conjunto(self):
        a_visitar = []
        cont = 0
        
        for i in self.adj_list:
            print(a_visitar)
            if i not in a_visitar:
                cont += 1
                a_visitar.extend(self.conjunto(i))
        return cont
    
    def conjunto(self, inicio, visitado=[]):
        if inicio in visitado:
            return visitado
        visitado.append(inicio)
        for node in self.adj_list[inicio]:
            self.conjunto(node)
        return visitado
    
    def ver_rutas(self, v1, v2, ruta, visitar=[]):
        if v1 not in self.adj_list and v2 not in self.adj_list:
            return
        
        if v1 not in visitar:
            visitar.append(v1)
        
        if v1 == v2:
            ruta.append(visitar[:])
            return ruta
        else:
            for vecionos in self.adj_list[v1]:
                self.ver_rutas(vecionos, v2, ruta, visitar)
                visitar.pop()
        return ruta
    
    def ver_rutas_con_peso(self, v1, v2, ruta, visitar=[], contar=0):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return
        
        if v1 not in visitar:
            visitar.append(v1)
        
        if v1 == v2:
            ruta.append((visitar[:], contar))
        
        else:
            if isinstance(v1, tuple):
                idx = v1[0]
            else:
                idx = v1
            
            for vecino, peso in self.adj_list[idx]:
                self.ver_rutas_con_peso(vecino, v2, ruta, visitar, contar + peso)
                visitar.pop()
        return visitar
    
    def existe_conexion(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return
        if v2 in self.adj_list[v1] or v1 in self.adj_list[v2]:
            return True
        return False

    def convertir_a_matriz(self):
        nuevo_grafo = []
        for vertice in self.adj_list:
            nuevo_grafo.add_vertex(vertice)
        
        for vertice in self.adj_list:
            for value  in self.adj_list[vertice]:
                nuevo_grafo.add_edge(vertice, value)
        return nuevo_grafo
    
    def mayor_alcance(self):
        visitar = {}
        maximo = 0
        valor = None
        for nodo in self.adj_list:
            visitar[nodo] = len(self.adj_list[nodo])
        for d in visitar:
            if maximo < visitar[d]:
                valor = d
                maximo = visitar[d]
        return valor
    
    def ciclo(self, v1=None, v2=None, visitado=[]):
        if v1 is None:
            v1 = 0
        visitado.append(v1)
        for node in self.adj_list[v1]:
            if node not in visitado:
                if self.ciclo(node, v1, visitado):
                    return True
            if node == v2:
                return True
        return False
    
    def __repr__(self):
        return str(self.adj_list)

g = Graph()
#g.adj_list = {
#    'A': ['B', 'C'],
#    'B': ['D'],
#    'C': ['D'],
#    'D': []
#}

#g.adj_list = {
#    'A': ['B'],
#    'B': ['C'],
#    'C': ['D'],
#    'D': []
#}

g.adj_list = {
  0: [1,2],
  1: [3],
  2: [3],
  3: []
}
ruta = []
print(g)
print(g.ver_rutas(0,3,ruta))
