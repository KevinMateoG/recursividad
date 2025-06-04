import sys
sys.path.append("Grafos")
from matriz_de_adyasencia import *
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
        return (False,cont)
    
    def tiene_ciclo(self):
        for vertice in self.adj_list:
            if self.verificar_ciclos(vertice):
                
                return True
    
    def cont_ciclo(self):
        for vertice in self.adj_list:
            if self.contat:
                
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
            return visitar
        else:
            for vecionos in self.adj_list[v1]:
                self.ver_rutas(vecionos, v2, ruta, visitar)
                visitar.pop()
        return visitar
    
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
        nuevo_grafo = Graph_matriz()
        for vertice in self.adj_list:
            nuevo_grafo.add_vertex(vertice)
        
        for vertice in self.adj_list:
            for value  in self.adj_list[vertice]:
                nuevo_grafo.add_edge(vertice, value)
        return nuevo_grafo
        ...


    def __repr__(self):
        return str(self.adj_list)

# 5 + 3

"""g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("d")
g.add_vertex("c")
g.add_vertex("e")
g.add_vertex("x")
g.add_edge("a", "b")
g.add_edge("b", "d")
g.add_edge("d", "b")
g.add_edge("b", "e")
g.add_edge("e", "c")
g.add_edge("e", "b")
g.add_edge("c", "x")
g.add_edge("c", "d")
g.add_edge("d", "a")"""
"""g.add_vertex("h")
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
g.add_edge("a", "l")"""
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B", True)
g.add_edge("A", "C", True)
g.add_edge("B", "D", True)
print(g.convertir_a_matriz())

"""g.add_vertex("A")
g.add_vertex("E")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "C",wigth=10)
g.add_edge("A", "E",wigth=20)
g.add_edge("E", "B",wigth=30)
g.add_edge("E", "D",wigth=40)
g.add_edge("B", "C",wigth=10)
g.add_edge("B", "D",wigth=20)
g.add_edge("D", "C",wigth=30)"""
#ruta = []
#g.ver_rutas_con_peso("A", "C", ruta)
#print(ruta)