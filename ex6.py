#programa que faz o dobro do numero escolhido, triplo e sua raiz quadrada
'''n1=int(input('digite um número '))
n2=n1*2
n3=n1*3
n4=n1**(1/2)

print('o resultado foi:\n {} número escolhido \n o seu dobro é de {}\n o seu triplo é de {}\n e a sua raiz é de {}'.format(n1,n2,n3,n4))'''


from math import sqrt
n1=int(input('digite um número '))
n2=n1*2
n3=n1*3
n4=sqrt(n1)
print('o resultado foi:\n {} número escolhido \n o seu dobro é de {}\n o seu triplo é de {}\n e a sua raiz é de {}'.format(n1,n2,n3,n4))

