'''from math import factorial
n1=int(input('Digie um número para calcular o fatorial '))
f=factorial(n1)
print('o fatorial de {} é {}'.format(n1,f))'''

n=int(input('Digite um numeoro para calcular o seu fatorial '))
c=n
f=1
print('calculando {}!'.format(n),end=' ')
while c>0:
    print('{}'.format(c), end=' ')
    print('X' if c>1 else ' = ', end='')
    f=f*c
    c-=1
print('O fatorial de {} é {}'.format(n,f))