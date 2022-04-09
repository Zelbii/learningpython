listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 5.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 20.32,
            'Canetas', 22.20,
            'Livro', 14.90)
print('-' * 40)
print('{:^40}'. format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print('{:.<30}'.format(listagem[c]), '€ {:.2f}'.format(listagem[c + 1]))
print('-' * 40)

#outra maneira de fazer, pulando de dois em dois

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)
