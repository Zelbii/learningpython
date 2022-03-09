from datetime import datetime


from datetime import date
totalmaior=0
totalmenor=0
for c in range(1,8):
    n=int(input('em que ano a {}º pessoa nasceu? '.format(c)))
    idade=date.today().year-n
    if idade>=18:
        totalmaior+=1
    else:
        totalmenor+=1
print('No total tivemos {} pessoas maiores de idade'.format(totalmaior))
print('No total tivemos {} pessoas menores de idade'.format(totalmenor))