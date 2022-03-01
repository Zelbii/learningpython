from datetime import date
n1=int(input('em que ano nasceu? '))
atual=date.today().year
idade=atual-n1
print('\033[1;33m Quem nasceu em {} tem {} em {} '.format(n1, idade, atual))
if idade<=9:
    Categoria='MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria='JUNIOR'
elif 19 < idade <= 25:
    categoria='SÊNIOR'
else:
    categoria='MASTERBLASTER'
print('Você tem {} logo a sua categoria é {}'.format(idade, categoria))