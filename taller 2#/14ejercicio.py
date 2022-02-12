"""
Datos de entrada
lectura_actual-->lac-->
lectura_anterior-->lan-->
Datos de salida
costo-->c-->int
"""

#entradas
from copyreg import constructor


lac=int(input("lectura actual:"))
lan=int(input("lectura anterior:"))
#caja negra
d=lan-lac
costo=""
if(d>0 and d<=100):
    costo=d*4600
if(d>=101 and d<=300):
    costo=d*80000
if(d>=301 and d<=500):
    costo=d*100000
if(d>=501):
    costo=d*120000
#salida
print("su costo sera: ", costo)