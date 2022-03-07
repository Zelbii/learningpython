n1=int(input('Digite um número '))
contador=0

for c in range(1, n1+1):
    if n1% c==0:
        contador+=1
print('o número {} foi divisivel {} vezes'.format(n1,contador))
if contador ==2:
    print('O número é primo')
else:
    print('O número não é primo')