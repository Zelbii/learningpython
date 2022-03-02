peso=float(input('Digite o seu Peso '))
altura=float(input('Digite a sua altura '))
imc=peso/(altura*altura)
if imc < 18.5:
    print('O seu IMC é de {:.2f} você está a baixo do peso'.format(imc))
elif 18.5<=imc<24.9:
    print('O seu IMC é de {:.2f} você está com o peso ideal '.format(imc))
elif 25<=imc<29.9:
    print('O seu IMC é de {:.2f} você está com sobrepeso '.format(imc))
elif 30<=imc<34.9:
    print('O seu IMC é de {:.2f} você está com Obesidade grau 1 '.format(imc))
elif 35<=imc<39.9:
    print('O seu IMC é de {:.2f} você está com obesidade grau 2 '.format(imc))
elif imc >=40:
    print('O seu IMC é de {:.2f} você está com obesidade grau 3' .format(imc))