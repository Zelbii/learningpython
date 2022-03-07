s=0 #fiz essas constantes para poder fazer as contas 
cont=0

for c in range(1,7):
    n1=int(input('digite o {}º número '.format(c)))
    if n1%2==0: #se os n1 for divisivel por 0 se resto faça aquilo
        s=s+n1
        cont=cont+1
print('Você digitou {} números Pares e a soma foi {}'.format(cont, s))
