'''import random

n1=str(input('primeiro '))
n2=str(input('segundo '))
n3=str(input('terceiro '))
n4=str(input('quarto '))

a=[n1, n2, n3, n4]

escolhido=random.choice(a)

print('o aluno escolhido foiiiiiiiii {}'.format(escolhido))'''

from random import choice

n1=str(input('primeiro'))
n2=str(input('segundo'))
n3=str(input('terceiro'))
n4=str(input('quarto'))

a=[n1, n2, n3, n4]

escolhido=choice(a)
print('o aluno escolhido foiiiiiiiii{}'.format(escolhido))
