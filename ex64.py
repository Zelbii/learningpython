n1=0
cont=0
total=0
n1=int(input('Digite um número, [se quiser terminar digitte 999] '))
while n1 !=999:
    n1=int(input('Digite um número, [se quiser terminar digitte 999] '))
    if n1 !=999:
        total+=n1
        cont+=1
print('Fim do programa, no total foram repetidas {} vezes sendo que a soma total é de {}'.format(cont,total))