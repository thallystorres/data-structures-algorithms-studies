#Função exemplo de aplicação de XOR e verificação de número desaparecido na lista, LeetCode 268

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """Função que encontra o número que falta numa lista de 0 até N

        Args:
            nums (list[int]): Lista a ser analisada

        Returns:
            int: Número faltando
        """

        #Para esse algoritmo fazemos um for simples verificando cada elemento do array e inputando-os numa variável e após isso verificamos se cada um deles possui uma contraparte no range do tamanho da lista

        a = 0

        for num in nums:
            a ^= num

        for i in range(len(nums)+1):
            a^= i
        
        return a