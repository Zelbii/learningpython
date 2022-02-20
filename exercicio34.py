s=float(input('Qual o seu salário? '))
if s <= 1250:
    print('o aumento do seu salário é de 15 porcento anteriormente era de {}, agora será de {} '.format(s, s*1.15))
else:
    print('o aumento do seu salário é de 10 porcento anteriormente era de {}, agora será de {} '.format(s, s*1.10))
