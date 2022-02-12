"""
Datos de entrada
cantidad_dinero-->dinero-->int
Datos de salida
salida de billetes y monedas -->int
"""
#entradas
cd = int(input("cantidad de dinero: "))
#caja negra-salida
bcien=(cd-cd%100000)/100000
cd=cd%100000
bcuen=(cd-cd%50000)/50000
cd=cd%50000
bve=(cd-cd%20000)/20000
cd=cd%20000
bdi=(cd-cd%10000)/10000
cd=cd%10000
bci=(cd-cd%5000)/5000
cd=cd%5000
bd=(cd-cd%2000)/2000
cd=cd%2000
bm=(cd-cd%1000)/1000
cd=cd%1000
mq=(cd-cd%500)/500
cd=cd%500
dn=(cd-cd%200)/200
cd=cd%200
dc=(cd-cd%100)/100
cd=cd%100
mcq=(cd-cd%50)/50
cd=cd%50
if(bcien>0):
    print("billetes de 100000: ", bcien)
elif(bcuen >0):
    print("billetes de 50000: ", bcuen)
elif(bve >0):
    print("billetes de 20000: ", bve)
elif(bdi >0):
    print("billetes de 10000: ", bdi)
elif(bci >0):
    print("billetes de 5000: ", bci)
elif(bd >0):
    print("billetes de 2000: ", bd)
elif(bm >0):
    print("billetes de 1000: ", bm)
elif(mq >0):
    print("monedas de 500: ", mq)
elif(dn >0):
    print("monedas de 200: ", dn)
elif(dc >0):
    print("monedas de 100: ", dc)
elif(mcq >0):
    print("monedas de 50: ", mcq)
