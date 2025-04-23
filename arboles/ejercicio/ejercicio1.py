import sys
sys.path.append("arboles")
from generalTree import *

def suma_de_nodos():
    ...

arbol = GeneralTree()
arbol.insert(10, 20)
arbol.insert(10, 7)
arbol.insert(7, 8)
arbol.insert(8 ,40)
print(arbol)
arbol.delete_with_child(10)
print(arbol.buscar(40))
print(arbol)