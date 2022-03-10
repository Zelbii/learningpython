# As duas fazem a mesma função, uma é com For e a outra com  While
from tkinter import N


'''for c in range(1,10):
    print(c)
print('fim')

c=1
while c <10:
    print(c)
    c=c+1
print('fim')'''

#-------------------------------------------------------------------

#While serve para essas questões, quando não sabemos quando será necessário para a repetição, nesse caso, 
#quando digitarmos 0, o programa para, caso contrário, não.
'''n=1
while n !=0: # n !=0 é a flag, o ponto te paragem.
    n=int(input('Digite um valor: '))
print('Fim')'''

'''n='S'
while n =='S':
    s=int(input('Digite um número: '))
    n=str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''

n=1
par=impar=0
while n !=0:
    n=int(input('digite um número '))
    if n%2==0:
        par=par+1
    else:
        impar=impar+1
    
print('Você digitou {} número pares e {} número  ímpares!'.format(par,impar))
