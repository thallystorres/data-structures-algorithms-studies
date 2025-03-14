# Função exemplo para inverter Linked List, LeetCode 206
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """Função que inverte uma linked list
        
        Args:
            head (ListNode): Linked List com primeiro ponto na head a ser invertida

        Returns:
            ListNode: Linked List invertida
        """
        new_list = None # criamos um Node imaginário que aponta inicialmente para o nada

        while head: # enquanto ainda houver algum Node na Linked List inicial
            next_node = head.next # o node após o head do momento é armazenado
            head.next = new_list # após isso, ele vira o novo new_list
            new_list = head # assim, o novo valor do new_list irá ser o próprio head
            head = next_node # e o head agora vai ser o node que antes era seu next
        
        return new_list
    

































    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_list = None

        while head:
            next_node = head.next
            new_list = head
            head.next = new_list
            head = next_node

        return new_list