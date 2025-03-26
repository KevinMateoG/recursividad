class Pila_vacia(Exception):
    """La pila esta vacia"""


class Stack:
    def __init__(self):
        self.stack: list[int] = []
    
    def push(self, elemento:int) -> None:
        self.stack.append(elemento)
    
    def pop(self) -> int:
        if len(self.stack) == 0:
            return Pila_vacia
        return self.stack.pop()
    
    def peek(self) -> int:
        if len(self.stack)== 0:
            return Pila_vacia()
        return self.stack[-1]
    
    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
    
    def __len__(self):
        return len(self.stack)
    
    
    def __repr__(self) -> str:
        return str(self.stack)