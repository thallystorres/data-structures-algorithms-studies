#Função exemplo para contar o número de bits 1 em um número

class Solution:
    def hammingWeight(self, n: int) -> int:
        """Função que contabiliza o número de bits 1 em um número

        Args:
            n (int): Número a ser analisado

        Return:
            int: Números de um's encontrados
        """
        res = 0 

        for i in range(32):
            if (n >> i) & 1:
                res += 1
        return res