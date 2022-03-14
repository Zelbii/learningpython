print('Gerador de PA')
print('_.-.'*19)
n1=int(input('Primeiro termo: '))
razão=int(input('Razão da PA: '))
termo=n1
cont=1
while cont <=10:
    print('{}-> '.format(termo),end='')
    termo=termo+razão
    cont=cont+1
print('fim')