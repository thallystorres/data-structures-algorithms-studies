#Operadores AND (&) OR (|) NOT (~) XOR (^)

# AND

#Se o bit analisado for 1 em ambas as casas, retorna 1, caso o contrário retorna 0

#Todo número AND 0 é 0

a = 5 & 0
b = 0 & 0
c = 4673167467813478614678146781346783467814678146783174687468 & 0
print(a, b, c)

#Todo número AND 1 verifica seu bit de paridade, caso seja 1 é ímpar, caso seja 0 é par

a = 1 & 1
b = 2 & 1
c = 0 & 1
d = 4 & 1
e = 46717467816784781784684678467167841687416784678416871 & 1
print(a,b,c,d,e)

#Todo número AND ele mesmo é ele mesmo

a = 5 & 5
b = 3 & 3
c = 2 & 2
d = 8 & 8
print(a,b,c,d)

# OR

#Se o bit analisado for 1 em qualquer casa retorna 1, caso contrário retorna 0

#Basicamente analisa todos os números e vai colocando 1 em tudo que vê pela frente, exceto nos zeros, é bom pra fazer bitmasking e juntar várias flags

# XOR

#Os bits par a par só retornam 1 se ambos forem diferentes entre si

#Todo número XOR com ele mesmo resulta em zero

# NOT

#Transforma o número no seu complementar somado que gera um número com todas as casas iguais a 1

#OBS: Esses operadores só funcionam para números inteiros