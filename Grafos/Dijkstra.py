def eliminar_nodo(grafo:dict[list], nodo_eliminar):
    if nodo_eliminar not in grafo:
        return grafo
    grafo.pop(nodo_eliminar)
    for i in grafo:
        if nodo_eliminar in grafo[i]:
            grafo[i].remove(nodo_eliminar)
    return grafo

def resto_de_conexiones(grafo:dict[list], caida,nodo= None, nodo2=None):
    eliminar_nodo(grafo, caida)
    if nodo is None:
        nodo = 0
    visitar = [nodo]
    for vert in grafo[nodo]:
        if nodo2 == vert:
            return True
        if vert not in visitar:
            if resto_de_conexiones(grafo, caida, vert, nodo):
                return True
    return False

grafo = {
  0: [1, 2],
  1: [0, 2],
  2: [0, 1, 3],
  3: [2]
}
caida = 1

print(resto_de_conexiones(grafo, caida))