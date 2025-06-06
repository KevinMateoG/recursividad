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

def numero_de_caminos(grafo, v1, v2, ruta=[], visitar=[]):
    if v1 and v2 not in grafo:
        return
    
    if v1 not in visitar:
        visitar.append(v1)

    if v1 == v2:
        ruta.append(visitar[:])
        return ruta
    else:
        for i in grafo[v1]:
            
            if i not in visitar:
                numero_de_caminos(grafo, i, v2, ruta, visitar)
                visitar.pop()
    return ruta

grafo = {
  0: [(1,4),(2,1)],
  1: [(3,1)],
  2: [(1,2),(3,5)],
  3: []
}

inicio = 0

print(numero_de_caminos(grafo, inicio))