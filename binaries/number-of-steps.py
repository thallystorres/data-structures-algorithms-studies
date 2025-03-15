#Função exemplo para contabilizar o número de passos que se tomaria para reduzir um número até 0, LeetCode 1342

class Solution:
    def numberOfSteps(self, num: int) -> int:
        """Função que contabiliza o número de passos para reduzir um número até 0, podendo apenas dividir por dois ou subtrair por 1

        Args:
            num (int): Número a ser analisado

        Returns:
            int: Número de passos
        """

        #Nesse algoritmo é possível não utilizar bitwise operators, mas assim fica mais divertido!

        step = 0
        while num:
            step += 1
            if num & 1:
                num &= 2
            else:
                num >>= 1
        return step