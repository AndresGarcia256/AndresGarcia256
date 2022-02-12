"""
Datos de entrada
temperatura---> t ---> float
Datos de salida
deporte --> deporte
"""
#entradas
t=float(input("temperatura en f°: "))

#caja negra
deporte=""
if(t>85 and t<=120 ):
    deporte="natacion"
elif(t>70 and t<=85 ):
    deporte="tennis"
elif(t>32 and t<=70 ):
    deporte="golf"
elif(t>10 and t<=32 ):
    deporte="esqui"
elif(t>0 and t<=10 ):
    deporte="marcha"
else:
    deporte="no se encuentra en le rango"  
# salida
print("su deporte es:", deporte)