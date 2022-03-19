sexo=str(input('Digite o seu Gênero [M/F]')).strip().upper()[0]
while sexo not in'MmFm':
    sexo=str(input('Digite um gênero válido, tente outra vez [M/F] ')).strip().upper() [0]
print('gênero registrado {} com sucesso'.format(sexo))