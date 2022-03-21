contidade=homen=mulher=0

while True:
    idade=int(input('Digite a sua idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo= str(input('Sexo:[M/F]')).strip().upper() [0]
    if sexo!='M' and sexo !='F':
        print('Sexo inválido, tente outra vez!')
    if sexo=='M':
        homen+=1
    if idade>=18:#contador de pessoas com mais de 18 anos
        contidade+=1
    if sexo=='F' and idade <=20:
        mulher+=1
    sair=' '
    while sair not in 'SN':
        sair=str(input('Digite [N] se quiser terminar o programa ')).strip().upper() [0]
    if sair=='N':
        break
print(f'''
O total de pessoas com mais de 18 anos: {contidade}
Ao todo temos {homen} homens cadastrados
E temos {mulher} mulheres com menos de 20 anos ''')



cont18 = conth = contm20 = 0
while True:
    print('-'*30)
    print('\tCADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('SEXO ÍNVALIDO. Tende novamente.')
    else: 
        if sexo == 'M' or 'F' and idade >= 18:
            cont18 += 1
        if sexo == 'M':
            conth += 1
        if sexo == 'F' and idade <= 20:
            contm20 += 1
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}\nAo todo temos {conth} Homens cadastrados\nE temos {contm20} mulheres com menos de 20 anos')