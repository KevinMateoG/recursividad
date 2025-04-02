class Node:
    def __init__(self, value):
        self.value: int = value
        self.next: Node = None

    def __repr__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0


    def append(self, value):
        new_node = Node(value)
        if(self.__size == 0):
            self.__head = new_node #d1
            self.__tail = new_node #d1
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def traverse(self, current_node=None, flag = True):
        if(flag):
            current_node = self.__head
        if(current_node is None):
            return
        print(current_node.value)
        current_node = current_node.next
        self.traverse(current_node, False)

    def delete_end(self):
        if(self.__size == 0):
            return
        elif(self.__size == 1):
            self.__head = None
            self.__tail = None
        else:
            #tengo que llegar al penúltimo
            current_node = self.__head
            while(current_node.next.next is not None):
                current_node = current_node.next
            current_node.next = None
            self.__tail = current_node
        self.__size -= 1

    def delete_first(self):
        if(self.__size == 0):
            return
        else:
            self.__head.value = None
            self.__head.next = None
        self.__size -= 1


    def __repr__(self):
        repr = ""
        current_node = self.__head
        while(current_node is not None):
            repr += str(current_node.value) + "->"
            current_node = current_node.next

        return f"{repr}"

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