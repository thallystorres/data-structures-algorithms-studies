#Estudos de operadores left shift e right shift

#Right Shift
#Desloca X casas a direita do número requerido, AKA divide por dois X vezes

def right_shift_custom(dividido: int, casas: int) -> int:

    for _ in range(casas):
        dividido //= 2
        
    return dividido

a = 10
print(a) # 10

a >>= 1
print(a) # 5

a >>= 1
print(a) # int(2.5)

a >>= 1
print(a) # 1

a >>= 1
print(a) # 0

a = 10

a >>= 4
print(a) # 0 também

#Left Shift
#Desloca X casas a esquerda do número requerido, AKA multiplica por dois X vezes

def left_shift_custom(multiplicando: int, casas: int) -> int:
    for _ in range(casas):
        multiplicando *= 2
    return multiplicando

b = 10
print(b) #10
b <<= 1
print(b) #20
b <<= 1
print(b) #40
b <<= 1
print(b) #80
b <<= 1
print(b) #160

b = 10

b <<= 4
print(b) #160


#OBS: Em algumas linguagens (Python não é uma delas) os inteiros tem número de bits pré-definidos, então é possível se locomover tanto num left shift que pode haver um "overflow" no número de casas, o que pode destoar da definição simplista de "left shift multiplica por dois"