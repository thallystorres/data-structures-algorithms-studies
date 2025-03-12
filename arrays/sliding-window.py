# Função exemplo pra Sliding Windows, LeetCode 3090
def maximumLengthSubstring(s: str) -> int:
    """ Função que tira o comprimento de substring com letras não repetidas mais de duas vezes.

    Arg:
        s (str): String a ser analizada.
    
    Return:
        int: tamanho máximo de substring com letras não repetidas mais de duas vezes.
    """
    # inicializando os ponteiros l, r para tirar o comprimento total da substring
    l,r = 0, 0
    # tamanho máximo inicializado como 1
    _max = 1
    # hashmap implementado para registrar cada aparição das letras
    d = {}
    # registro do primeiro caracter
    d[s[0]] = 1
    # r tem que ser menor que o índice do último caracter da string
    while r < len(s) - 1:
        # aumento iterável de r
        r += 1
        # se o caracter de s no índice r não estiver no hashmap, introduz no hashmap
        if not d.get(s[r]):
            d[s[r]] = 1
        # se já estiver, adiciona +1 no registro de hashmap
        else:
            d[s[r]] += 1
        # se passar de duas aparições do caracter, reduz o tamanho da substring analisada em 1 e retira 1 do valor no hashmap
        while d[s[r]] == 3:
            d[s[l]] -= 1
            l += 1
        # max definido pela max() entre ele mesmo e o tamanho da substring 
        _max = max(_max, r-l+1)
    return _max