class EmptyQueue(Exception):
    ...

class Queue:
    def __init__(self):
        self.__queue: list[int] = []

    # agrega al final de la cola
    def enqueue(self, element: int):
        self.__queue.append(element)

# retorna y elimina el primer elemento que entró
    def dequeue(self) -> int:
        if(len(self.__queue) == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.__queue.pop(0)

    # retorna el primer elemento que entró
    def first(self) -> int:
        if(len(self.__queue) == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.__queue[0]

    def __repr__(self):
        return str(self.__queue)

    def __len__(self):
        return len(self.__queue)