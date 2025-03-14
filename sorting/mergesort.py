#OBS: O mergesort geralmente é aplicado em ordenação de linked lists, enquanto o quicksort é usando no geral em arrays e listas. Vale salientar que nem sempre isso é verdade!

#Time complexity:
# - Best case: O(n log n)
# - Average case: O(n log n)
# - Worst case: O(n log n)

#Space complexity:
# - Best case: O(n)
# - Average case: O(n)
# - Worst case: O(n)

#obs: Sempre tem O(n) como complexidade espacial por justamente analisar e armazenar as subdivisões da linked list até o fim

# Possui o funcionamento em duas etapas:
# 1- Divide a linked list ao meio ao ponto de chegar no nodo mais central (chamado de folha)
# 2-Ao separar toda  linked list em várias LLs menores minimamente ordenadas, junta todas novamente de forma em que todas se encaixem em seus respectivos locais

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head: Node) -> Node:
    """Função que localiza o meio de uma Linked List

    Args:
        head (ListNode): Linked List a ser analisada

    Returns:
        ListNode: Nodo específico que se encontra no centro da Linked List
    """
    slow = head
    fast = head.next

    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(l1: Node, l2: Node) -> Node:
    """Função que junta e ordena duas linked lists da menor pra maior

    Args:
        l1 (Node): Head da primeira linked list a ser analisada
        l2 (Node): Head da segunda linked list a ser analisada

    Returns:
        Node: Head da linked list analisada e ordenada
    """

    #Nesse algoritmo, primeiro se inicializa uma head vazia que irá servir como largada da nova linked list, e assim, adicionamos a cada iteração do While um novo nodo à linked list a ser retornada, verificando se esse nodo será da primeira ou da segunda LL

    head = Node()
    tail = head

    while l1 and l2:
    
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
    
        else:
            tail.next = l2
            l2 = l2.next
        
        tail = tail.next
    
    tail.next = l1 or l2

    return head.next

def mergesort(head: Node) -> Node:
    """Função mergesort propriamente dita

    Args:
        head (Node): Head da LL a ser ordenada

    Returns:
        Node: Head da LL já ordenada
    """

    #Faremos aqui um algoritmo de recursão em que o passo base é verificar se ainda há algo a ser ordenado (caso tenha ao menos dois nodos na LL). Caso não atinja o passo base, divide-se a LL no meio e chamamos a função novamente para cada lado da LL e após isso, juntamos.

    if not head or not head.next:
        return head
    
    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None
    
    left = mergesort(head)
    right = mergesort(after_middle)
    
    return merge(left,right)

def build_linked_list(values: list)-> Node:
    """Função que constroi uma linked list com elementos de um array passado

    Args:
        Values (list): Lista de elementos passados que irão popular a LL
    
    Returns:
        Node: Retorna o head da LL que irá ser construida com os valores
    """

    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head

def print_linked_list(head: Node) -> None:
    """Função que irá printar na tela cada valor da linked list passada sem esgotá-la

    Args:
        Head (Node): Cabeça da LL a ser printada

    Returns:
    """
    result = []
    current = head

    while current:
        result.append(current.value)
        current = current.next
        
    print(result)
