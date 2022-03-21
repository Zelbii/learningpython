total=totmil=menor=cont=0
while True:
    produto=str(input('Nome do produto: '))
    preço=float(input('Preço: '))
    cont+=1
    total+=preço
    if total>1000:
        totmil+=1
    if cont==1:
        menor=preço
    else:
        if preço<menor:
            menor=preço

    sair=' '
    while sair not in 'SN':
        sair=str(input('Deseja continuar? Aperte [N] para parar o programa. ')).strip().upper()[0]
    if sair=='N':
        break
print(f'''
O total da compra foi de {total:.2f}
Temos {totmil} produtos custando mais que 1000 euros
O produto mais barato custa {menor:.2f}
A média dos produtos foi de {total/cont :.2f}''')