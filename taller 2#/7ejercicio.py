"""
Datos de entrada
numero de km->km->float

Datos de salida
cobor->cb->float
"""
#entradas
km=float(input("cantidad de kilometros: "))
#caja negra
x=-1000+km
if(km<300):
    va=50000  
elif(km>300 and km<=1000):
    va=70000
elif(km==1000):
    va=150000  
elif(km>1000):
    va=150000+(x*9000)
#salida
print("se pagara", va)