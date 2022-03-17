resp= 'S'
média=0
soma=0
cont=0
while resp in 'Ss':
    num=int(input('Digite um número: '))
    resp=str(input('Quer continuar? [S/N]')).upper().strip() [0]
    soma+=num   
    cont+=1
media=soma/cont
print('Acabou, digitou {} vezes sendo que a soma é {} assim sendo a média é de {}'.format(cont,soma,media))