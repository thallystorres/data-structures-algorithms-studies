#Função exemplo para mergear duas LLs ordenadas, LeetCode 21
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Função que junta duas LLs ordenadas

        Args:
            list1 (ListNode): Head da primeira LL ser analizada
            list2 (ListNode): Head da segunda LL ser analizada

        Returns:
            ListNode: Head da lista mergeada
        """

        #Nesse algoritmo, primeiro inicializamos uma nova LL vazia que servirá para armazenar a ordenação de ambas LLs, verificando a cada iteração qual o próximo valor de cada LL é menor entre si até chegarmos no fim da primeira LL e por fim juntamos com o resto da lista que sobrou

        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2

        return head.next