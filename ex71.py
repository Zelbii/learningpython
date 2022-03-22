'''nota_cinqueta=nota_vinte=nota_dez=nota_um=0
dinheiro=int(input('Qual o valor que deseja sacar? '))
while True:
    while dinheiro -50>=0:
        dinheiro-=50
        nota_cinqueta+=1
    while dinheiro -20>=0:
        dinheiro-=20
        nota_vinte+=1
    while dinheiro -10>=0:
        dinheiro-=10
        nota_dez+=1
    while dinheiro-1>=0:
        dinheiro-=1
        nota_um+=1
    break
if nota_cinqueta !=0:
    print(f'Total de {nota_cinqueta} cédulas de 50€')
elif nota_vinte !=0:
    print(f'Total de {nota_vinte} cédulas de 20€')
elif nota_dez !=0:
    print(f'Total de {nota_dez} cédulas de 10€')
elif nota_um !=0:
    print(f'Total de {nota_um} cedula de 1€')
else:
    print('Inválido')'''


#código do guanabara
print('='*30)
print('{:^30}'.format('BANCO Zelbi'))
print('='*30)

valor=int(input('Que valor você quer sacar? € '))
total=valor
céd=50
totcéd=0
while True:
    if total>=céd:
        total-=céd
        totcéd=1
    else:
        if totcéd>0:
            print(f'Total de {totcéd} cédula de € {céd}')
        if céd ==50:
            céd=20
        elif céd==20:
            céd=10
        elif céd ==10:
            céd=1
        totcéd=0
        if total==0:
            break
print('='*30)

print('Volte sempre ao vanco Zelbi')