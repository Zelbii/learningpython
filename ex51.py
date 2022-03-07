n1=int(input('Primeiro termo '))
n2=int(input('razão '))
décimo=n1+(10-1)*n2
for c in range(n1, décimo+n2, n2):
    print('{}'.format(c), end='->')
print('acabou')