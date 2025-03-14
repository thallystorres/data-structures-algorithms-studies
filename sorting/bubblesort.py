#Time complexity:
# - Best case: O(n)
# - Average case: O(n²)
# - Worst case: O(n²)

#Space complexity: O(1)


def bubbleSort(arr: list) -> None:
    """Sua implementação basicamente consiste num nested-loop que compara elemento i com cada elemento j da lista e troca-os de posição

    Args:
        arr (list): Lista a ser ordenada
    
    Returns:
        É inplace, ou seja, ela não retorna nada, ela modifica a lista em memória mesmo.
    """
    
    n = len(arr)
    for _ in arr:
        is_sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if is_sorted == True:
            return

#OBS: É criada uma variável is_sorted para verificar se a lista já está ordenada sem precisar fazer vários loops desnecessários pelo array