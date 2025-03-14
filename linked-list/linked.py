# Implementando uma linked list do zero
# Lembrando: Linked List pode ser doubly ou não
# Linked List clássica: tem um head, um tail e elementos centrais. Cada elemento possui um ponteiro apontando para o próximo
# Linked List Doubly: tem um head, um tail e elementos centrais. A diferença é que cada elemento possui DOIS ponteiros, um apontando para o próximo na ordem head to tail (next) e um para o próximo na ordem tail to head (previous)
class Node: # Nó de cada valor da LL
    def __init__(self, value):
        self.value = value
        self.next = None # Pq None?
        self.prev = None # Pq None?
        # Analisa comigo, se há apenas um Node, como ele vai ter um ponteiro pro próximo ou pro anterior, se há apenas ele? Sacou? isso não é uma LL ainda, é apenas o nó de uma

class DoublyLinkedList: # DLL propriamente dita
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value): # add um novo head
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_to_back(self, value): # add um novo tail
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_front(self): # removendo o front
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value
    
    def remove_from_back(self): # removendo o back
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed_value