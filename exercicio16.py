from math import trunc # importei da biblioteca Math a função Trunc
num=float(input('digite um número '))
print('o valor digitado foi {} o valor inteiro é de {}'.format(num, trunc(num))) # utilizei a função trunc que serve para dar o número inteiro sem o ponto

#as vezes não precisa pegar uma biblioteca, as vezes as funções internar têm como resolver seu problema
num=float(input('digite um número '))
print('o valor digite {} e a sua porção inteira é {}'.format(num, int(num)))