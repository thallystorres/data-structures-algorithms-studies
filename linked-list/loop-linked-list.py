# Agora vamos tentar verificar se há um loop de ponteiros na linked list, estranho né?
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution: # aqui nós vamos usar um algoritmo de velocidade que nem na questão do middle LL
    def hasCycle(self, head: ListNode) -> bool:
        fast = head # um que andará duas casas
        slow = head # outro que andará apenas uma

        while fast and fast.next: # enquanto o fast não for None e nem seu .next
            fast = fast.next.next # pula duas casas
            slow = slow.next # pula apenas uma
            if slow == fast: # se eles se encontrarem retorna True
                return True
        return False # caso o while finalizar então não há loop, retorna False
    
#OBS: Esse tipo de algoritmo tem um nome! Ele se chama Floyd's Tortoise and Hare Algorithm (referenciando à fábula da tartaruga e a lebre)