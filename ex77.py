palavras=('ensinar','ler', 'verao', 'esquisito','testar', 'ficar',' tentar', 'verificar')
for p in palavras:
    print(f'na palavra {p.upper()}, temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')