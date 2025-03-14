import time
import random
import psutil
import os
from pympler import asizeof

# Quicksort In-Place (usando Partition - Lomuto)
def quicksort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quicksort com List Comprehension (cria novas listas a cada chamada)
def quicksort_list_comprehension(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_list_comprehension(left) + middle + quicksort_list_comprehension(right)

# Função para medir memória do processo
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Em MB

# Criando uma lista grande aleatória
N = 10_000  # Tamanho da lista para teste
arr1 = [random.randint(0, 100000) for _ in range(N)]
arr2 = arr1[:]  # Copiando para garantir que ambas tenham a mesma entrada

# Medindo Quicksort In-Place
mem_before = get_memory_usage()
size_before = asizeof.asizeof(arr1)

start_time = time.time()
quicksort_inplace(arr1, 0, len(arr1) - 1)
time_inplace = time.time() - start_time

mem_after = get_memory_usage()
size_after = asizeof.asizeof(arr1)

# Medindo Quicksort com List Comprehension
mem_before_lc = get_memory_usage()
size_before_lc = asizeof.asizeof(arr2)

start_time = time.time()
arr2_sorted = quicksort_list_comprehension(arr2)
time_lc = time.time() - start_time

mem_after_lc = get_memory_usage()
size_after_lc = asizeof.asizeof(arr2_sorted)

# Resultados
print(f"Quicksort In-Place:")
print(f"- Tempo de execução: {time_inplace:.6f} segundos")
print(f"- Memória do processo antes: {mem_before:.2f} MB")
print(f"- Memória do processo depois: {mem_after:.2f} MB")
print(f"- Tamanho da lista antes: {size_before / 1024:.2f} KB")
print(f"- Tamanho da lista depois: {size_after / 1024:.2f} KB")
print()

print(f"Quicksort List Comprehension:")
print(f"- Tempo de execução: {time_lc:.6f} segundos")
print(f"- Memória do processo antes: {mem_before_lc:.2f} MB")
print(f"- Memória do processo depois: {mem_after_lc:.2f} MB")
print(f"- Tamanho da lista antes: {size_before_lc / 1024:.2f} KB")
print(f"- Tamanho da lista depois: {size_after_lc / 1024:.2f} KB")
