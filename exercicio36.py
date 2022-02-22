casa=float(input('Qual o valor da casa que deseja comprar? '))
sal=float(input('Qual o seu salário atual? '))
anos=int(input('em quantos anos é que deseja pagar o empréstimo? '))

mensal=casa/(anos*12)
mini=sal*(30/100)

if mensal <= mini:
    print('A casa que pretende comprar tem o valor de {} \nPara pagar essa casa em {} a mensalidade será de {} \nEmprestimo APROVADO  '.format(casa,anos,mensal))
else:
    print('A casa que pretende comprar tem o valor de {} \nPara pagar essa casa em {:.2f} a mensalidade será de {} sendo menor ou igual a 30 porcento do seu salário \nempréstimo NEGADO '.format(casa,anos,mensal))