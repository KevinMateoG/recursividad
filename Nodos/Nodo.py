def ErrorListaVacia(Exception):
    """lista vacia"""


class Node:
    def __init__(self, value):
        self.value: int = value
        self.next: Node = None

    def __repr__(self):
        return str(self.value)

def imprimir_todos_los_nodos(nodo: Node):
    while nodo != None:
        print(nodo)
        nodo = nodo.next

def buscar_elemento(nodo: Node, numero_buscar: int):
    while nodo != None:
        if nodo.value == numero_buscar:
            return True
        nodo = nodo.next
    return False


def agregar_final(nodo: Node, valor):
    while nodo != None:
        nodo = nodo.next
"""    return nodo.next = valor"""
    
a = Node(10)
b = Node(7)
c = Node(1)
d = Node(6)
e = Node(8)
f = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
"""imprimir_todos_los_nodos(a)"""
print(buscar_elemento(a, 9))