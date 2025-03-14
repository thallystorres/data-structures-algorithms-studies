# Função exemplo para two-pointer, LeetCode 557
def revereWords(s: str) -> str:
    """Função que inverte cada palavra de uma string
    
    Args:
        s (str): String a ser invertida
    
    
    Returns:
        (str): String invertida
    """
    # inicialização de ponteiros de início e final de palavra
    l, r = 0, 0
    # inicialização de string vazia que seram adicionadas as palavras invertidas
    res = ''
    # enquanto r não seja o fim da string
    while r < len(s):
        # se s[r] não for uma string de espaço separando palavras, aumenta-se o índice
        if s[r] != ' ':
            r += 1
        # se não, se adiciona à resposta a substring palavra invertida, seleciona como início l e fim r+1 para garantir o espaço separando cada palavra. [::-1] é o método em python para inverter posição de string
        else:
            res += s[l:r+1][::-1]
            # aumentando índice de r
            r += 1
            # leando l para a primeira letra da palavra
            l = r
    # quando o while para, ainda faltará a última palavra, assim adiciona-se um espaço e a última palavra invertida
    res += ' '
    res += s[l:r+2][::-1]
    # retorna pulando a primeira casa já que a primeira palavra invertida possui um espaço em branco no seu início
    return res[1:]
