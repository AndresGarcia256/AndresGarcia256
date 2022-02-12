"""
Datos de entrada
P-->p-->int
Q-->q-->int
Datos de salida
"""
#entradas
P=int(input("ingrese valor de P: "))
Q=int(input("ingrese valor de Q: "))
#caja negra
h=(P**3)+(Q**4)-(2*P**2)
ecuacion=""
if(h>680):
    print("satisfacen la expresion", Q,P)
elif(h<680):
    print("no satisface la expresion", Q,P)
#salida
print("el resultado es ademas ", h)
