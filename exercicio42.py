s1=float(input('o primeiro segmento tem '))
s2=float(input('o segundo segmento tem '))
s3=float(input('o terceiro segmento tem '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um trinângulo!', end='')
    if s1==s2==s3:
        print('EQUILÁTERO ')
    elif s1!=s2!=s3!=s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo!')