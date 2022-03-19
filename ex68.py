from random import randint
from time import sleep
cont=soma=0
print('=-=-'*20)
print('Vamos jogar Par ou ímpar?')
print('=-=-'*20)

while True:
    computador=randint(0,10)
    jogador=int(input('Digite um número! '))
    soma=computador+jogador
    escolha=str(input('Digite [P/I] para escolher entre PAR ou ÍMPAR ')).strip().upper()
    if escolha in 'Pp':
        if soma %2==0:
            sleep(1)
            print('Você venceu ')
            cont+=1
        else:
            sleep(1)
            print('Você perdeu')
            print('=-=-'*20)
            print(f'A sua sequência de vitórias é de {cont}')
            print('=-=-'*20)
            break
    else:
        if soma %2==1:
            sleep(1)
            print('Você venceu')
            cont+=1
        else:
            sleep(1)
            print('Você perdeu')
            print(f'sua sequência de vitórias é de {cont}')
            break