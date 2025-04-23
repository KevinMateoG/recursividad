class BinaryNode():
    def __init__(self, value):
        self.value = value
        self.left_child : BinaryNode = None
        self.right_child: BinaryNode = None

class BinarySearchTree():
    def __init__(self):
        self.root: BinaryNode = None
    
    def insert(self,value, current=None):
        if current is None:
            current = self.root

        if self.root is None:
            self.root = BinaryNode(value)
            return 
        
        else:
            
            if current.value == value:
                return
            
            if current.value > value:
                if current.left_child is None:
                    current.left_child = BinaryNode(value)
                    return
                else:
                    self.insert(value, current.left_child)
                
            elif current.value < value:
                if current.right_child is None:
                    current.right_child = BinaryNode(value)
                    return
                else:
                    self.insert(value, current.right_child)
        
    def search(self, value, current=None):
        if current is None:
            current = self.root
        if self.root is None:
            return False 
        else:
            if current.value == value:
                return True
            if current.value < value:
                if current.right_child is not None:
                    self.search(value, current.right_child)
                else:
                    return False

            elif current.value > value:
                if current.left_child is not None:
                    self.search(value, current.left_child)
                else:
                    return False

    def terna(self, n, current=None):
        if current is None:
            current = self.root
        if self.root.value == current.value:
            first = current.value
        else:
            ...
# puntos llevo 4
    def print(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right_child:
            self.print(node.right_child, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left_child:
            self.print(node.left_child, prefix + ("    " if is_left else "│   "), True)


tree = BinarySearchTree()
tree.insert(3)
tree.insert(5)
tree.insert(6)
tree.insert(1)
tree.insert(7)
tree.insert(-1)
tree.insert(3)
tree.insert(2)
tree.print(tree.root)
tree.search(2)
tree.search(90)