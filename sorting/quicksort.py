import psutil
import os
#Aplicação de um QuickSort sem list comprehension (é superior pela alocação menor de memória, funcionar em linguagens que não são Python...)

#Time complexity:
# - Best case: O(n log n)
# - Average case: O(n log n)
# - Worst case: O(n²)

#Space complexity:
# - Best case: O(log n)
# - Average case: O(log n)
# - Worst case: O(n)

#OBS: Caso se escolha um pivô ruim para a aplicação do algoritmo, então entraremos no WCS (Worst Case Scenario) temporal e espacial

def partition(arr: list[int], left: int, right: int) -> int:
    """Função que cria uma partição que remonta um subarray ordenando os elementos em maior ou menor que o pivô selecionado

    Args:
        arr (list[int]): Sub-lista a ser ordenada
        left: Ponteiro mais a esquerda que irá analisar a parte inicial do array ou sub-array
        right: Ponteiro mais a direita que irá analisar a parte final do array ou sub-array
    
    Returns:
        int: Retorna assim o índice final do pivô
    """
        
    pivot = arr[right] #Podemos mudar isso aqui? escolher pivô sempre com o mesmo índice não é recomendado
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j] , arr[i]
    i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quicksort(arr: list[int], left: int, right: int):
    """Algoritmo de dividir e conquistar (DC), baseado em separar subarrays de um array e ordena-los recursivamente

    Args:
        arr (list[int]): Lista a ser ordenada
        left: Ponteiro mais a esquerda que irá analisar a parte inicial do array ou sub-array
        right: Ponteiro mais a direita que irá analisar a parte final do array ou sub-array
    
    Returns:
        É inplace, ou seja, ela não retorna nada, ela modifica a lista em memória mesmo.
    """

    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)

process = psutil.Process(os.getpid())

a = [1,2, 3,4, 1, 3, 8, 3, 1010, 12, -1, 0, 0, 0, 1010, 1010, 1011]
quicksort(a, 0, len(a)-1)
print(a)
print(f"Memória usada pelo processo: {process.memory_info().rss / (1024 * 1024):.2f} MB")
