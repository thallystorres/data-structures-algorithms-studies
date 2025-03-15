#Função exemplo para encontrar o número sem par em uma lista, LeetCode 136

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """Função que analisa uma lista e verifica qual item dela não tem um mesmo representante em par

        Args:
            nums (list[int]): Lista a ser analisada

        Returns:
            int: Número faltando
        """


        a = 0
        for num in nums:
            a ^= num
        return a