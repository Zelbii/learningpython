n1=str(input('coloca teu nome ai ')).strip()
print('analisando...')
print('o seu nome em grande fica {}'.format(n1.upper()))
print('o seu nome em grande fica {}'.format(n1.lower()))
print('o seu nome tem no total {}'.format(len(n1)-n1.count(' ')))
print('o seu primeiro nome tem {}'.format(n1.find(' ')))