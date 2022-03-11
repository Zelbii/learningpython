'''n1=int(input('estou pensando em um número de 0 a 5, tente advinhar'))
if n1 == 3:
    print('você ganhou')
else:
    print('você errou!')'''


from random import randint # da biblioteca random importei a função radiant que serve para o computador escolher um número da lista
from time import sleep
computador=randint(0,10) #fiz a variavel camputador receber 0 ou 10 da função radiant
print('-._.-'*29)
print('pense em um número entre [0 e 10] -> ')
print('-._.-'*29)
acertou=False
tentativa=0
while not acertou:
    n1=int(input('digite um número inteiro entre [0 e 10] -> ')) # fiz o jogador interagir com o programa, pedindo para ele colocar um número de 0 a 10
    tentativa=tentativa+1
    print('processando...')
    sleep (0.5)

    if n1==computador: # se o jogador acertar o mesmo número do computador ele ganha
        print('você acertou!!! pensamos os dois em {} '.format(computador))
        acertou=True
    else: #caso contrário ele perde
        if n1<computador:#essa parte if, serva para ajudar o jogador a saber se tem que colocar um número maior ou menor
            print('mais um pouquinho! ')
        else:
            print('é menos um pouco! ')
print ('Você acertou depois da {} tentativa '.format(tentativa))#caso o jogador acerte, vai aparecer a quantidade de tentativas que levou para ele acertar