


import calendar
from datetime import date
ano = int(input('Digite o ano: '))
ano6 = calendar.isleap(ano)
if ano==0:
    ano=date.today().year
if ano6 is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')



from datetime import date
ano=int(input('digite o ano que precisa analisar digite 0 caso precise ver a data atual do seu pc '))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100 !=0 or ano%400==0: # se o número for divisivel por 4=0 por 100 !=0 OU 400=0 ELE É BISSEXTO
    print('o {} é BISSEXTO '.format(ano))
else:
    print('o ano {} não é BISSEXTO'.format(ano))
