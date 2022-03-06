print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')

for c in range(0,6): #no python ele vai contar do 1 até o 5 e no 6 ele para, por isso que colocamos o 0, para fazer do 5 até o 5 contando 6 vezes de OI
    print('oi')

print('fim')#vai escrever oi 6 vezes e depois dar print 'FIM

for c in range(0,6):
    print('oi')
    print('fim') #aqui o programa vai escrever oi fim 6 vezes só porque o "print('fim')" está na mesma camada que o "print('oi')"

for c in range (1,6):#contagem crescente de 1 até 5, ele ignora o 6
    print(c)
print('fim')

for c in range (6,0,-1):# contagem decrescente de 6 até 1 o -1 é de quanto em quanto que vai ser pulado, nesse caso vai ser de -1, sendo assim vai decrescer
    print(c)
print('FIM')


i=int(input('início: '))#insira o inicio da contagem
f=int(input('Fim: '))#insira o fim da contagem
p=int(input('Passo: '))#de quanto em quanto que vai pular o valor
for c in range(i,f+1,p):#0 f+1 é o fim da contagem, nesse caso queremos que ele pare de contar depois de F, sendo assim f+1
    print(c)
print('FIM')

for c in range(0,3):
    n=int(input('Digite um valor: '))#podemos colocar input dentro de FOR
print('fim')

s=0#atribuindo valor de s=0 
for c in range(0,4):
    n=int(input('Digite um valor: '))#possibilitando a entrada de 3 valores podemos fazer o somatório deles
    s+=n#somatório dos valores (0+n)
print('o somatório de todos os valores foi {}'.format(s))
