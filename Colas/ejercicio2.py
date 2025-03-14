from colas_normales import *
def filtrado_mensajes(colas: Queue):
    aux = Queue()
    for _ in range(len(colas)):
        primer = colas.first()
        for j in range(len(colas)):
            colas.dequeue()
            if primer == colas.first:
                    ...