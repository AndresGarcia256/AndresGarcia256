"""
Datos de entrada
sueldo del trabajador --> sd --> float
Datos de salida
nuevo sueldo -->ns--> float
"""
#entradas
sd=float(input("ingrese su sueldo:"))
#caja negra
if(sd<=900000):
    ns=sd*1.15
elif(sd>900000):
    ns=sd*1.12
#salida
print("su nuevo sueldo es:", ns)
