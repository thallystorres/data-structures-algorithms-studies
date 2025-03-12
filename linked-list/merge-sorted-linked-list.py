# agora vamos tentar juntar duas linked list ordenadas!
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode: # okay, vou ter que repassar por aqui mais tarde, achei meio confusa essa resolução
        dummy = ListNode() # primeiro criamos um "dummy" (pelo visto é tipo um boneco de treinamento) da classe ListNode, ou seja, ele vai ser uma Linked List
        cur = dummy # depois criamos um ponteiro para nos certificar em que parte da linked list estamos

        while list1 and list2: #enquanto ambas as listas não tiverem terminado faremos o loop
            if list1.val > list2.val: # verificamos se valor de uma é maior que a outra
                cur.next = list2 # e depois colocamos o no próximo valor do dummy o valor do menor entre os dois valores passados
                list2 = list2.next # e pulamos uma casinha
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next # após isso pulamos uma casinha para ser preenchida
        
        if list1: # se ainda sobrar uma lista a ser finalizada, o próximo valor do dummy será o seu último
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next # depois retornamos o dummy.next, já que o head é um None