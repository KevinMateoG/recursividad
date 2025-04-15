class Node:
    def __init__(self, value):
        self.value: int = value
        self.children: list[Node] = []

    def __repr__(self):
        return f"{self.value} -> {self.children}"

class GeneralTree:
    def __init__(self):
        self.root: Node = None
    
    def insert(self, parent, child, flag = True, current = None):
        if flag == True:
            current = self.root
            
        if self.root == None:
            self.root = Node(parent)
            node_child = Node(child)
            self.root.children.append(node_child)
            return 
        
        else:
            if current.value == parent:
                node_child = Node(child)
                current.children.append(node_child)
                return True
            
            for ch in current.children:
                if self.insert(parent,child, flag=False, current=ch) is True:
                    return True
    
    def buscar(self, child, current = None):
        if current is None:
            current = self.root
        
        if self.root == None:
            return False
        
        if current.value == child:
            return True
        
        else:
            for ch in current.children:
                if self.buscar(child, current= ch):
                    return True
        return False
        
    def delete_with_child(self, value, current= None):
        if current is None:
            current = self.root
        
        if self.root == None:
            return "no hay que eliminar"
        
        if self.root.value == value:
            self.root = None
            return

        for ch in current.children:
            if ch.value == value:
                current.children.remove(ch)
                return True
            if self.delete_with_child(value, ch):
                return True
    
    def __repr__(self):
        return f"{self.root}"

arbol = GeneralTree()
arbol.insert(10, 20)
arbol.insert(10, 7)
arbol.insert(7, 8)
arbol.insert(8,40)
print(arbol)
arbol.delete_with_child(10)
print(arbol.buscar(40))
print(arbol)