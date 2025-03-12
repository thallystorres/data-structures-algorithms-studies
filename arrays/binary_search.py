# !!!IMPORTANTE!!!
# Pode ser usada em array e binary tree
# Só funciona se os itens estiverem ordenados
# Complexidade temporal: O(log n)
# Complexidade espacial: O(1)
def binarySearch(arr: list[int], target: int, ip = 0, fp = None) -> int:
    """Implementação de Binary Search.

    Args:
        arr (list[int]): lista/array de ints a ser verificado.
        target (int): elemento procurado na lista.
        ip (int): initial pointer, ou seja, ponteiro que irá ser localizado no início da squência.
        fp (int): final pointer, ou seja, ponteiro que irá ser localizado no final da sequência.
    
    Returns:
        int: Índice em que target se encontra no array, caso não esteja contido, -1.
    """
    # Verifica se fp foi atribuído a um valor, caso não, fp é atribuido ao índice do último item
    if fp is None:
        fp = len(arr) - 1
    # OBS: não é ip < fp, caso ip == fp ainda haverá mais um passo a ser feito
    while ip <= fp:
        # mid inicializado no meio entre ip e fp, superior a usar int((fp + ip) / 2), evitando criar float 
        mid = (fp + ip) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] > target:
            # reduz o array, retirando a maior metade
            fp = mid - 1
        elif arr[mid] < target:
            # reduz o array, retirando a menor metade
            ip = mid + 1
    return -1