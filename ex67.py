

while True:
    print('_.-.'*29)
    n1=int(input('quer ver a tabuada de qual valor? '))
    if n1<0:
        break
    print('_.-.'*29)
    for c in range (1,11):
        print(f'{n1} X {c} = {n1*c}')
print('FIM')



