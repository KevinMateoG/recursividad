from Nodos.Nodo import *
class EmptyQueue(Exception):
    ...

class Queue:
    def __init__(self):
        self.__queue: LinkedList = LinkedList()

    # agrega al final de la cola
    def enqueue(self, element: int):
        self.__queue.append(element)

    # retorna y elimina el primer elemento que entró
    def dequeue(self) -> int:
        if(self.__queue.__size == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.__queue.delete_first()

    # retorna el primer elemento que entró
    def first(self) -> int:
        if(self.__queue.__size == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.__queue[0]

    def __repr__(self):
        return str(self.__queue)

    def __len__(self):
        return len(self.__queue)