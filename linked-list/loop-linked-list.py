# Função exemplo para verificar se uma Linked List é infinita, LeetCode 141
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        """Função verificadora de ciclo
        
        Args:
            head (ListNode): Linked List que irá ser verificada

        Returns:
            bool: True se houver ciclo falso caso não houver
        """
        
        fast = head # um ponteiro para o nodo que andará duas casas
        slow = head # um ponteiro para o nodo que andará apenas uma casa

        #Caso em algum momento esses nodos se encontrarem no loop, então haverá sim um ciclo, pois eles iriam se esbarrar

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    
#OBS: Esse tipo de algoritmo tem um nome! Ele se chama Floyd's Tortoise and Hare Algorithm (referenciando à fábula da tartaruga e a lebre)





























class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution: # aqui nós vamos usar um algoritmo de velocidade que nem na questão do middle LL
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False