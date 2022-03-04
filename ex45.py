from random import randint
from time import sleep
itens=('Pedra', 'Papel', 'Tesoura')
computador=randint(0, 2)
print('Suas opções: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA ')
n1=int(input('Qual será a sua jogada? '))
print('_.-.'*15)
print('pedra')
sleep(2)
print('papel')
sleep(2)
print('tesouraaaaaaaaaaa')
if computador ==0: # O computador jogou PEDRA
    if n1==0:
        print('\033[1;33ma jogada empatou!')
    elif n1==1:
        print('\033[1;32mVocê ganhou!!!!')
    elif n1==2:
        print('\033[1;31mVocê perdeu!!!!')
elif computador ==1: # O computador jogou PAPEL  
    if n1==0:
        print('\033[1;31mVoce perdeu!!!!')
    elif n1==1:
        print('a jogada empatou!')
    elif n1==2:
        print('\033[1;32mVocê ganhou!!!!')
elif computador ==2: # o Computador jogou TESOURA   
    if n1==0:
        print('\033[1;32mVocê ganhou!!!!')
    elif n1==1:
        print('\033[1;31mVocê perdeu!!!!')
    elif n1==2:
        print('\033[1;33mA jogada empatou!')
else:
    print('Opção inválida')
print('_.-.'*15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[n1]))