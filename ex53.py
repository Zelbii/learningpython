#palavra é um palindromo?

#sem for
'''n1=str(input('Digite uma frase ')).upper().replace(' ','')
if n1==n1[::-1]:
    print('a frase é um palindromo')
else:
    print('a frase não é um palindromo')'''

n1=str(input('Digite uma frase: ')).strip().upper()
palavras=n1.split()
junto=''.join(palavras)
inverso='*'
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('temos um políndromo!')
else:
    print('não temos um políndromo')