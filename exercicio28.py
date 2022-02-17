'''n1=int(input('estou pensando em um número de 0 a 5, tente advinhar'))
if n1 == 3:
    print('você ganhou')
else:
    print('você errou!')'''


from random import randint # da biblioteca random importei a função radiant
from time import sleep
computador=randint(0,5) #fiz a variavel camputador receber 0 ou 5 da função radiant
print('-._.-'*29)
print('pense em um número entre 0 e 5')
print('-._.-'*29)
n1=int(input('digite um número inteiro entre 0 e 5 ')) # fiz o jogador interagir com o programa, pedindo para ele colocar um número de 0 a 5
print('processando...')
sleep (2)

if n1==computador: # se o jogador acertar o mesmo número do computador ele ganha
    print('você acertou!!! pensamos os dois em {}'.format(computador))
else: #caso contrário ele perde
    print('você errou feio errou rudeeeee eu pensei em {} e você em {}'.format(computador, n1))
print ('-_-_-FIM-_-_-')