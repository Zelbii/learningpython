print('Gerador de PA')
print('_.-.'*29)
n1=int(input('Primeiro termo: '))
razão=int(input('Razão da PA: '))
termo=n1
cont=1
total=0
mais=10
while n2!=0:
    total=total+mais
    while cont <=total:
        print('{}-> '.format(termo),end='')
        termo=termo+razão
        cont=cont+1
    n2=int(input('Quantos termos você quer adicionar? '))
print('progressão finalizado com {} termos'.format(total))
