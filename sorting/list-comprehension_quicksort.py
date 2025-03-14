import psutil
import os
#Usando list comprehension

# Ao contrário da implementação clássica do quicksort, essa implementação com list comprehension não é inplace, gerando um número desnecessário de listas em memória para completá-lo

def quicksort_lc(arr: list[int]) -> list[int]:
    """Algoritmo de dividir e conquistar (DC), baseado em separar subarrays de um array e ordena-los recursivamente

    Args:
        arr (list[int]): Lista a ser ordenada
        left: Ponteiro mais a esquerda que irá analisar a parte inicial do array ou sub-array
        right: Ponteiro mais a direita que irá analisar a parte final do array ou sub-array
    
    Returns:
        list: Lista final retornada ao fim da recursão
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    menores = [i for i in arr[1:] if i <= pivot]
    maiores = [i for i in arr[1:] if i > pivot]
    return quicksort_lc(menores) + [pivot] + quicksort_lc(maiores)

process = psutil.Process(os.getpid())

a = [1,2, 3,4, 1, 3, 8, 3, 1010, 12, -1, 0, 0, 0, 1010, 1010, 1011]

print(quicksort_lc(a))
print(f"Memória usada pelo processo: {process.memory_info().rss / (1024 * 1024):.2f} MB")