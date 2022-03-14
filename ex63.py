n1=int(input('Quantos termos quer mostrar? '))

contador=1
anterior=0
próximo=1
soma=1

while contador<=n1:
    print(anterior, end='-')
    contador=contador+1
    soma=próximo+anterior
    anterior=próximo
    próximo=soma
print('FIM')