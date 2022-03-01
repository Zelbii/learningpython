n1=float(input('Qual a nota que obteve no primeiro teste? '))
n2=float(input('Qual a nota que obteve no segundo teste? '))
m=(n1+n2)/2
if m<8:
    print('\033[1;31m obteve {} e {} reprovado terrá que ir a exame {} '.format(n1, n2,m))
elif m>=9.5:
    print('\033[1;32m obteve {} e {} Parabéns!! você passou com {}'.format(n1,n2,m))
elif 8 <= m < 9.4:
    print('\033[1;33m obteve {} e {} será permitida a realização do segundo teste, sua média é de {}, '.format(n1, n2, m))