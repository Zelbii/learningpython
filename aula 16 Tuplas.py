lanche=('hamburguer', 'suco', 'Pizza', 'Pudim')                #(Tuplas), [lista] {Dicionario}
print(lanche[2]) #mostra o lanche 2 apenas
print(lanche[0:2]) #mostra o lanche 0 e 1, quando chega no 2 ele para
print(lanche[1:]) #mostra o lanche 1 até o fim da tupla
print(lanche[-1]) #mostra o lanche 4, porque ele começa a fazer a contagem de trás para frente
print(lanche[1:3]) #mostra o lanche 1 e 2 e desconsidera o 3
len(lanche)# conta a quantidade de elementos que há dentro da tupla

for c in lanche:
    print(f'eu vou comer {c}') #o for vai mostrar 1 de cada vez, até chegar no Pudim e quando isso acontecer o programa acaba
print('fim')

#tuplas são imutaveis, para atriuir um valor dentro do progrmaa tenho que parar ele e mudar manualmente

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}') # duas maneiras de fazer for em tuplas dependendo da maneira que eu for fazer o programa é melhor usar a segunda.
print('fim')

for cont in range(0, len(lanche)): 
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Ei vou comer {comida} na posição {pos}')

pessoa=('Elber', 22, 'M',116.3) #posso ter dados dentro da tuplas de diferentes tipos
print(pessoa)

a=(2,5,4)
b=(6,8,1,2)
c=b+a
print(c)
print(c.index(8)) #index(x)mostra em qual posição ta o teu número escolhido
print(c.index(2)) # aqui vão mostrar a primeira posição, a segunda n vai, pra isso usamos o metodo de baixo
print(c.index(2,4)) #para ver a posição apartir da posição 2 