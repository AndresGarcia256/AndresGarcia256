"""
Datos de entrada
valor de A --> a --> int
valor de B --> b --> int
valor de C --> c --> int
valor de D --> d --> int
Datos de salida
valor de la ecuacion --> ve --> str
"""
#entradas
a=int(input("ingrese valor de a"))
b=int(input("ingrese valor de b"))
c=int(input("ingrese valor de c"))
d=int(input("ingrese valor de d"))
#caja negra
if(d==0):
    ve=(a-c)**2
elif(d>0):
    ve=((a-b)**3)/d
#salida
print("el valor de la expresion es:", ve)