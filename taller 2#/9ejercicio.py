"""
Datos de entrada
valor de la venta-->valor-->venta
nombre--> n--> string
Datos de salida
nombre--> n--> string
monto compra --> mc --> float
monto a pagar --> map --> float 
descuento --> des --> float
"""
#entradas
valor=float(input("valor de la venta: "))
n=str(input("su nombre:"))
#caja negra
compra=""
if(valor<50000):
    compra=valor
    des=valor
elif(valor>50000 and valor<=100000):
    compra=valor*0.95
    des=valor*0.05
elif(valor>100000 and valor<=700000):
    compra=valor*0.89
    des=valor*0.11
elif(valor>700000 and valor<=1500000):
    compra=valor*0.82
    des=valor*0.18
elif(valor>1500000):
    compra=valor*0.75
    des=valor*0.25
#salida
print("su nombre es ", n)
print("su compra fue de:", valor)
print("su compra tendra un valor de: ",compra)
print("el decuento fue de: ", des)
