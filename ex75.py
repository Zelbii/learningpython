a=int(input('Digite um número '))
b=int(input('Digite mais uma vez '))
c=int(input('Digite mais uma vez '))
d=int(input('uma ultima vez '))
tupla=(a,b,c,d)
cont=0
pares=tupla
print(f'Você digitou os valores {tupla}')

for contador9 in tupla:
    if contador9==9:
        cont+=1
print(f'O valor 9 apareceu {cont} vezes ')

if 3 in tupla:
    print(f'O número 3 aparece na {tupla.index(3)+1}º posição ')
else:
    print('não contêm o número 3 nessa tupla')
county=0
countx=0

for pares in tupla:
    if pares %2==0:
        county+=1
    else:
        countx+=1
print(f'Os valores pares digitados foram {county} ')
print(f'Os valores impares digitados foram {countx} ')     