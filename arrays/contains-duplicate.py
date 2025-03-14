# Função para exercitar Sliding Window, LeetCode 219
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """Função que verifica se há itens iguais em uma distância máxima de "k"

    Args:
        nums (list[int]): lista a ser verificada.
        k (int): distância máxima.
    
    Returns:
        bool: Há ou não itens iguais separados pela distância k ou menor.
    """
    # inicializa hashmap que vai registrar a última aparição do item na lista
    s = {}
    # iteração para verificar cada item da lista
    for i in range(len(nums)):
        # verificação da exigência da questão
        if nums[i] in s and abs(s[nums[i]] - i) <= k:
            return True
        # atualização da aparição do item no hashmap
        s[nums[i]] = i

    return False