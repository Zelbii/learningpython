from time import sleep
print('SEJA MUITO BEM VINDO')
sleep(2)
print('_.-.'*30)
print('É um cliente sortudo! por ser a dua primeira compra receberá um desconto se fizer uma viagem maior que 200km')
n1=float(input('Insira a quantidade de Km que irá fazer '))
if n1 >200:
    print(' recebeu a promoção! a viagem de {} terá  o valor de {}€'.format(n1,n1*0.45))
else:
    print('está preste a fazer uma viagem de {} terá o valor de {}€'.format(n1,n1*0.50))
return n1