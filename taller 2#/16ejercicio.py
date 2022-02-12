"""
Datos de entrada
valor de A --> A --> int
valor de B --> B --> int
valor de C --> C --> int
Datos de salida
valor de x--> x --> str
valor de x2--> x2 -->str
"""
#entradas
a=int(input("valor de a"))
b=int(input("valor de b"))
c=int(input("valor de c"))
d= b**2-4*a*c

#caja negra
if(d==0):
    x=x2=-b/(2*a)
    print("el valor de x1 es:", str(x), "y el valor de x2 es:", str(x2))
elif(d>0):
    x=(-b+(b**2-4*a*c))/(2*a)
    x2=(-b-(b**2-4*a*c))/(2*a)
    print("el valor de x1 es:", str(x), "y el valor de x2 es:", str(x2))
else:
    print("no tiene solucion en los reales")
#salida