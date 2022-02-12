'''import math
a=float(input('insira um ângulo '))
seno=math.sin(math.radians(a))
print('o ângulo de {} tem o SENO de {:.2f} '.format(a, seno))

coseno=math.cos(math.radians(a))
print('o ângulo de {} tem o COSENO de {:.2f} '.format(a, coseno))

tangente=math.tan(math.radians(a))
print('o ângulo de {} tem a TANGENTE de {:.2f} '.format (a,tangente))'''

from math import radians, sin, cos, tan
a=float(input('insira um ângulo '))
seno=sin(radians(a))
print('o ângulo de {} tem o SENO de {:.2f} '.format(a, seno))

coseno=cos(radians(a))
print('o ângulo de {} tem o COSENO de {:.2f} '.format(a, coseno))

tangente=tan(radians(a))
print('o ângulo de {} tem a TANGENTE de {:.2f} '.format (a,tangente))