from time import sleep
print('Qual a velocidade atual do carro? ')
sleep(2)
v=float(input('digite aqui '))
if v <=80:
    print('Vá com Deus meu parça')
else: 
    multa=(v-80)*7
    print('ih mané, perdeu, passa pra ca {} euros você foi taxado! '.format(multa))
    print('vá com Deus meu parça')
print('FIM')