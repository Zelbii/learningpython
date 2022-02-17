#carro.sega()
#carro.esquerda()
#carro.siga()
#carro.direito()
#carro.siga()
#carro.direito()
#carro.siga()
#carro.esquerdo()
#carro.siga()
#carro.pare()

#todas essas ordens são sequiênciais, acontecem de cima para baixo, não tem como pular etapa, só tem 1 caminha ou seja é uma estrutura sequêncial

#carro.siga() aqui tem 2 opções, ou vira a direito ou a esquerda
    #carroesquerda()        carro.direito()
    #carro.siga()           carro.siga()
    #carro.direito()        carro.esqueda()
    #carro.siga()           carro.siga()
    #carro.direito()        carro.esquerda()
    #carro.esquerda()       carro.siga()
    #carro.siga()           carro.pare()
    #carro.direito()
    #carro.siga()
    #carro.pare()

'''tempo=int(input('Quantos anos tem o seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')'''



'''tempo=int(input('Quantos anos tem o seu carro? '))
print('carro novo'if tempo <=3 else 'carro velho')
print('--FIM--')'''

'''n1=(input('Qual o seu nome? ')).upper()
if n1=='ELBER':
    print('que nome lindooooooo <3')
else:
    print('não é tão lindo esse nome.')
print('Bom dia {}'.format(n1))'''

n1=float(input('digite a sua primeira nota '))
n2=float(input('digite a sua segunda nota '))
m=(n1+n2)/2

if m >=9.5:
    print('aprovado com sucesso ')
else:
    print('reprovado')


