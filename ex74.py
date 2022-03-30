from random import sample

a=tuple(sample(range(10),5))
print (a)
print(f'O maior valor é {max(a)}')
print(f'O menor valor é {min(a)}')