#Clássica TwoSum, LeetCode 001
def twoSum(nums: list[int], target: int) -> list[int]:
    """Função que da o índice de dois itens que somados são o target final

    Args:
        nums (list[int]): Lista a ter seus itens analisados
        target (int): Número alvo a ser localizado

    Return:
        list[int]: Lista dos índices em que se encontram os números somados entre si
    
    """

    # dicionário que irá registrar cada ocorrência primária dos dígitos
    d = {}
    # loop que irá registrar cada dígito da lista no dicionário
    for index in range(len(nums)):
        d[nums[index]] = index
    # loop que irá verificar se cada número do dicionário tem um complemento par o target
    for i in range(len(nums)):
        complement = target - nums[i]
        # ao encontrar um complemento que não seja ele mesmo, retorna a lista com ambos indices
        if complement in d and d[complement] != i:
            return [i, d[complement]]
    # caso não encontre um complemento válido, retorna uma lista vazia
    return []
