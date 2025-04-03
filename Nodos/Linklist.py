
class Node:
    def __init__(self, value, next = None):
        self.value: int = value
        self.next: Node = next

class Linklist:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def delet_end(self):
        if self.__size == 0:
            print("no hay nada")
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            current_node = self.__head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            self.__tail = None
        self.__size -= 1

    def __repr__(self):
        rep = ""
        current_node = self.__head
        while current_node is not None:
            rep += str(current_node.value) + "->"
            current_node = current_node.next
        return rep

ll = Linklist()
ll.append(1)
ll.append(5)
ll.append(7)
ll.append(8)
ll.delet_end()
print(ll)