# e agora? vamo tentar achar o centro de uma linked list?
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # o ponto da solução é basicamente uma questão de velocidade em física
        # veja, se um carro anda x/h e outro anda 2x/h, então quer dizer que no tempo 1h o carro 1 vai ter andado a metade do carro 2
        # desse modo, se fizermos um ponteiro apontando pro head e fazer os dois avançarem de uma em uma casa, ambos vão chegar no fim no mesmo momento, mas se um se mover pulando uma casa, então vai chegar no fim enquanto o outro está no meio

        ahead = head # apontando para o mesmo local de origem

        while ahead and ahead.next: # enquanto o ahead ainda existir e ainda possuir um elemento à frente
            ahead = ahead.next.next # pula duas casas
            head = head.next # pula apenas uma
        
        return head # retorna o mais lento
    
# OBS: no while existe essas duas condições justamente pra garantir que o caso de número par na linked list funcionar, permitindo que ahead.next.next não quebre apontando para o next de um None