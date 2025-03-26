class Node:
    def __init__(self, value):
        self.value: int = value
        self.next: Node = None

    def __repr__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def append(self, value):
        ...

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
    if nodo == None:
        nodo = valor
    return nodo

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
imprimir_todos_los_nodos(a)
print(buscar_elemento(a, 9))
print(agregar_final(a, 8))