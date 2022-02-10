#esse programa é um conversor de medidas
m1=float(input('coloque a sua medida em metros '))
km=m1/1000
hm=m1/100
dam=m1/10
dm=m1*10
cm=m1*100
mm=m1*1000

print('{}km\n {}hm\n {}dam\n {}dm\n {}cm\n {}mm\n'.format(km,hm,dam,dm,cm,mm))