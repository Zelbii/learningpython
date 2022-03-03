print('=======Lojas Chaves=======')

n1=float(input('Digite o valor da sua compra '))
print('[1] à vista dinheiro/cheque\n[2] à vista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão')
n2=int(input('como pretende fazer o pagamento? '))
if n2==1:
    compra=n1*0.90
    print('a sua compra que inicialmente era de {} teve um desconto 10% e o valor final é de {:.2f}'.format(n1,compra))
elif n2==2:
    compra=n1*0.95
    print('a sua compra que inicialmente era de {} tede um desconto de 5% e o valor final é de {:.2f}'.format(n1, compra))
elif n2==3:
    parcela=n1/2
    print('A sua compra que inicialmente era de {} parcelando em 2x o valor da parcela é de {}'.format(n1,parcela))
elif n2==4:
    n3=int(input('Em quantas prestações pretende pagar? '))
    parcela=n1*1.20/n3
    preço=n1*1.20
    print('A sua compra que inicialmente era de {} pagando em {} as parcelas finais serão de {} totalizando o valor de {}'.format(n1,n3,parcela,preço))
else:
    print('opção inválida, escolha um número de 1 a 4 ')
