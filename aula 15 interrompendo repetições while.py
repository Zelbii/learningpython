cont=1
while cont <=10:
    print(cont, '->', end=' ')
    cont+=1
print('Acabou') 

cont=1
while True: #esse comando true vai fazer com que o laço de repetição seja infinito
    print(cont, '->', end=' ')
    cont+=1
print('Acabou') # com o comando TRUE esse print('Acabou) nunca vai acontecer pois não tem como sair do laço'''

n1= cont=0
while cont <3:
    n1=int(input('Digite um número'))
    cont+=3 
#até aqui não precisamos do loop infinito, pois temos flags que indicam quando parar, nesse caso em cima, quando der 3 ciclos de looping
n=s=0
while n !=999:
    n=int(input('Digite um número: '))
    s+=n
s-=999
print('a soma vale {} '.format(s)) #o que temos aqui é uma gambiarra, o 999 ta como numero de paragem, e para ele não somar quando for digitado para parar, colocamos ele a subtrair 999

n=s=0
while True:
    n=int(input('Digite um número: '))
    if n==999:#se for 999 o programa vai parar e não vai somar o 999, ele ignora a soma do 999 e interpreta como um comando de paragem
        break
    s+=n
print('A soma vale {} '.format(s)) #isso não vai nunca chegar nessa parte, porque ta com looping infinito la em cima

nome='Elber'
idade=22
print(f'o {nome} tem {idade} anos.') #PYTHON 3
print('o {} tem {} anos.'.format(nome, idade)) #PYTHON 3
print('o %s tem %d anos.'%(nome,idade)) #PYTHON 2