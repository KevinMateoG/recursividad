class EmptyStack(Exception):
    ...

class Stack:
    def __init__(self):
        self.__stack: list[int] = []

    # agrega al final de la pila ( tope )
    def push(self, element: int):
        self.__stack.append(element)

    # retorna y elimina el primer elemento que entró
    def pop(self) -> int:
        if(len(self.__stack) == 0):
            raise EmptyStack("Pila Vacía...")
        return self.__stack.pop()

    # retorna el último elemento que entró (top) -- LIFO: Last In First Out
    def peek(self) -> int:
        if(len(self.__stack) == 0):
            raise EmptyStack("Pila Vacía...")
        return self.__stack[-1]

    def __repr__(self):
        return str(self.__stack)

    def __len__(self):
        return len(self.__stack)