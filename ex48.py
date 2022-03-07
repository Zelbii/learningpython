soma = 0
for i in range(1, 501, 2):
  if i%3 == 0:
    soma += i
print("A soma dos múltiplos ímpares de 3 entre 1 e 500 é {}".format(soma))

