d=int(input('temos o custo de 60 euros diarios,por quantos dias o carro ficou alugado? '))
km=float(input('por cada km percorrido, será cobrado 0,15 centimos, quantos km foram percorridos? '))
custod=60
kmt=0.15
custot=(d*custod)+(km*kmt)

print('o seu carro ficou alugado {}, durante esse tempo, percorreu {}, senddo assim o custo total é de {}'.format(d,km,custot))