"""
Datos de entrada
iversion 
reinversion de interes
Datos de salida
dinero total
valor de las ganancias
valor total 
"""
#entradas
inversion=float(input("capital invertido:"))
i=float(input("tasa de intereses:"))
#caja negra
p=inversion*(i/100)
total=((p+inversion)*i)
intereses=""
if(100000<p ):  
    print("el valor de las ganancias es", str(p) )
else:
    print("el valor de la cuenta es", str(total) )
#salida