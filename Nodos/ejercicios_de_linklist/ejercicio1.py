import sys
sys.path.append("Nodos")
from Linklist import *

def invertir_lista_enlazada(lista: Linklist, nodo_siguiente=None):
    if nodo_siguiente is None:
        nodo_siguiente = lista.__head
    new_node = Linklist()
    while nodo_siguiente.next is not None:
        nodo_siguiente = nodo_siguiente.next
    new_node.append(nodo_siguiente.value)
    invertir_lista_enlazada(lista, nodo_siguiente)

ll = Linklist()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)
print(invertir_lista_enlazada(ll))
