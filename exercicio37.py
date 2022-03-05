num=int(input('digite um número inteiro: '))
print('''escolha uma das bases para a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para DECIMAL''')

opção=int(input('Sua opção: '))

if opção==1:
    print('{} convertido para BINÀRIO é igual a {}'.format(num, bin(num)[2:])) #[2:] é para começar a contar depois do 2 número porque no python as funções BIN OCT HEX elas começam com caracteres estranhos tipo Bi110011
elif opção==2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('opção inválida. tenta novamento')
