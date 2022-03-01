from datetime import date
atual=date.today().year
n1=int(input('Digite o seu ano de nascimento '))
idade=atual-n1
print('\033[1;33m Quem nasceu em {} tem {} em {} '.format(n1, idade, atual))
if idade==18:
    print('\033[1;33m você deve se alistar imediatamente ')
elif idade<18:
    saldo=18-idade
    print('\033[1;32m ainda faltam {} para o seu alistamento '.format(saldo))
    ano=atual+saldo
    print('o seu ano de alistamento  será em {} '.format(ano))
elif idade>18:
    saldo=idade-18
    print('\033[1;31m você já deveria ter se alistado faz {} anos!! vai rápido procurar o quartel mais próximo de ti '.format(saldo))
    ano=atual-saldo
    print('o seu ano de alistamento foi em {} '.format(ano))
