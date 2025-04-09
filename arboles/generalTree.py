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
        
        if current.value == parent:
            node_child = Node(child)
            current.children.append(node_child)
            return
        
        else:
            for ch in current.children:
                self.insert(parent,child, flag=False, current=ch)
    
    def __repr__(self):
        return f"{self.root}"

arbol = GeneralTree()
arbol.insert(10, 20)
arbol.insert(10, 7)
arbol.insert(7, 8)
arbol.insert(8,40)
print(arbol)

