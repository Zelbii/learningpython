from this import d


num=int(input('digite um número '))
u=num//1 % 10
d=num//10 % 10
c=num//100 % 10
m=num//1000 % 10
print('analisando o número {}'.format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))