from binary_search import binarySearch
# Usa a função binarySearch em sua composição
# Complexidade temporal: O(log n)
# Complexidade espacial: O(1)
def exponentialSearch(arr: list[int], target: int) -> int:
    """Implementação de Exponential Search
    
    Args:
        arr (list[int]): lista/array a ser verificado.
        target (int): elemento procurado na lista.

    Returns:
        int: Índice em que target se encontra no array, caso não esteja contido, -1.
    """
    # verifica se o target não está na primeira posição, reduzindo a velocidade nos melhores casos possíveis
    if arr[0] == target:
        return 0
    # inicializa tamanho do array e o ponteiro i que irá passar de forma exponencial 2^x pelo array
    tamanho = len(arr)
    i = 1
    while i < tamanho and arr[i] < target:
        # cada iteração multiplica por 2 até achar um elemento maior que target, assim analisando o subarray em que arr[i] está como último elemento
        i *= 2
    if arr[i] == target:
        # caso de alguma forma arr[i] seja o target, retorna i (improvável)
        return i
    # aplicação de Binary Search no subarray
    return binarySearch(arr, target, i//2, min(tamanho-1, i))