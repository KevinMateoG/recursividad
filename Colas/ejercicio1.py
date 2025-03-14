from colas_normales import Queue

def buscar_elemento(cola: Queue, elemento):
    encontrado = False
    aux = Queue()
    for _ in range(len(cola)):
        if elemento == cola.first():
            encontrado = True
        aux.enqueue(cola.dequeue())
    
    for _ in range(len(aux)):
        cola.enqueue(aux.dequeue())
    
    return encontrado

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5) #og: [1,2,3][4,5]#aux:
print(q)
print(buscar_elemento(q, 5)) # True
print(q)