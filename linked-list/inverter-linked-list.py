# Pô aqui tu vai basicamente ser esquizofrênico e criar um head imaginário e ir invertendo os ponteiros de cada elemento, se liga
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_list = None # aqui começa a esquizofrenia, a gente vai criar um head imaginário que será apontado pelo head antigo

        while head: # enquanto ainda houver head
            next_node = head.next # o node após o head do momento é armazenado
            head.next = new_list # após isso, ele vira o novo new_list
            new_list = head # assim, o novo valor do new_list irá ser o próprio head
            head = next_node # e o head agora vai ser o node que antes era seu next
        
        return new_list