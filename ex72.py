numero=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoite','dezenove','vinte')
while True:
    num=int(input('Digite Um número de 0 a 20: '))
    if 0<= num <=20:
        break
    print('tente novamente. ',end=' ')
print(f'Voce digitou {numero[num]}')