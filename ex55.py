lista=[]
for c in range (1,7):
    n=float(input('O peso da {}º pessoa: '.format(c)))

    lista+=[n]
print('_.-.'*19)
print('O maior peso é {}Kg ',max(lista))
print('O menor peso é {}Kg ',min(lista))