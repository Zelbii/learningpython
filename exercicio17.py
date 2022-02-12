'''n1=float(input('qual a medida do cateto oposto '))
n2=float(input('qual o comprimento do cateto adjacente '))
n3=(n1**2+n2**2)**(1/2)
print('a hipotenusa é de {:.2F}'.format(n3))'''

import math # from math import hypot

co=float(input('Comprimento do cateto oposto '))
ca=float(input('Comprimento do cateto adjacente '))
h1=math.hypot(co, ca)

print('a hipotenusa vai medir {:.2f}'.format(h1))