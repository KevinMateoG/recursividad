from Recursividad.pilas import *

def imprimir_elementos_de_lista(pila: Stack):
    aux = Stack()
    for _ in range(len(pila)):
        p = pila.pop()
        aux.push(p)
        print(p)
    
    for _ in range(len(aux)):
        pila.push(aux.pop())
        
q = Stack()
q.push(5)
q.push(57)
q.push(9)
q.push(3)
imprimir_elementos_de_lista(q)
print(q)