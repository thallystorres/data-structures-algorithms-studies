# Bora implementar uma linked list DO ZERO???
# Lembrando: Linked List pode ser doubly ou não
# Linked List clássica: tem um head, um tail e elementos centrais. Cada elemento possui um ponteiro apontando para o próximo
# Linked List Doubly: tem um head, um tail e elementos centrais. A diferença é que cada elemento possui DOIS ponteiros, um apontando para o próximo na ordem head to tail (next) e um para o próximo na ordem tail to head (previous)
class Node: # Nó de cada valor da ll
    def __init__(self, value):
        self.value = value
        self.next = None # Pq None?
        self.prev = None # Pq None???
        # Analisa comigo, se há apenas um Node, como ele vai ter um ponteiro pro próximo ou pro anterior, se há apenas ele? Sacou? isso não é uma LL ainda, é apenas o nó de uma

class DoublyLinkedList: # DLL propriamente dita
    def __init__(self):
        self.head = None # None pq ela ainda não tem nenhum nó
        self.tail = None # None pq ela ainda não tem nenhum nó

    def add_to_front(self, value): # add um novo head
        new_node = Node(value) # elemento node
        new_node.next = self.head # o next do novo node será o head antigo (caso não houver vai ser um None)
        if self.head: # claro, se houver head antigo
            self.head.prev = new_node # o node antes do antigo head vira o novo valor
        else:
            self.tail = new_node # o tail E o head vão ser o novo node, já que tem só um :P
        self.head = new_node

    def add_to_back(self, value): # add um novo tail
        new_node = Node(value) # elemento node
        new_node.prev = self.tail # o prev do novo node será o antigo tail (caso não houver vai ser um None)
        if self.tail: #claro, se houver tail antigo
            self.tail.next = new_node # o node depois do antigo tail vira o novo valor
        else:
            self.head = new_node # o head E o tail vão ser o novo node, já que só tem um :P
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