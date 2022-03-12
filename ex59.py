from time import sleep


n1=int(input('Digite um número '))
n2=int(input('Digite outro número '))
opção=0
while opção !=5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] Novos números
    [5] Sair do programa''')
    opção=int(input('Qual é a sua opção '))
    if opção==1:
        n3=n1+n2
        print('A soma de {} mais {} é igual a {}'.format(n1,n2,n3))
    elif opção==2:
        n3=n1*n2
        print('O produto de {} com {} é igual a {} '.format(n1,n2,n3))
    elif opção==3:
        if n1>n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n2>n1:
            print('{} é maior que {}'.format(n2,n1))
        else:
            print('O valor do primeiro número é {} o valor do segundo número é {}, sendo assim são iguais')
    elif opção==4:
        n1=int(input('Digite um número '))
        n2=int(input('Digite outro número '))
    elif opção==5:
        print('Finalizando')
        sleep(1)
print('Fim do programa!')