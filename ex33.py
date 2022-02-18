from re import A


a=float(input('digite o primeiro número '))
b=float(input('digite o segundo número '))
c=float(input('digite o terceiro número '))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
if b>a and b>c:
    maior=b
if c>a and c>a:
    maior=c
print('o menor número é {}'.format(menor))
print('o maior número é {}'.format(maior))

n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)

print('O menor número é {}'.format(lista_ordenada[0]))
print ('O maior número é {}'.format(lista_ordenada[2]))