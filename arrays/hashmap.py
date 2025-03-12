# Função exemplo para problemas com Hashmap, LeetCode 387
def firstUniqChar(s: str) -> int:
    """Função que retorna o primeiro caracter que não se repete na string.

    Arg:
        s (str): String a ser analisada.
    
    Return:
        int: Índice do caracter que não se repete na string, caso não há, retorna -1.
    """
    # inicializando hashmap para relacionar string, index de primeira aparição e número de aparições
    hashmap = {}
    # iteração que analisa cada caracter da string e seu índice
    for index, ch in enumerate(s):
        # se o caracter não tiver aparecido antes, cria uma posição no hashmap para ele
        if not hashmap.get(ch):
            hashmap[ch] = [index, 1]
        # se não, adiciona mais um ao número de aparições
        else:
            hashmap[ch][1] += 1
    # iteração que analisa cada item do hashmap
    for value in hashmap.values():
        # já que os hashmaps em python são implementados em ordem de inicialização, não precisamos nos preocupar em ordenar os caracteres
        if value[1] == 1:
            # caso o número de aparições seja 1, retorna o índice do caracter
            return value[0]
    return -1