"""
Datos de entrada
cargo --> cargo --> str
sueldo --> s --> float
Datos de salida
saldo burto --> sd --> float
cargo --> cargo --> str
"""
#entradas
s=float(input("ingrese su salario: "))
cargo=str(input("cual es su cargo"))
#caja negra
sd=""
if(s==900000):
    sd=900000*1.60
if(s==2000000):
    sd=2000000*1.40
if(s==3600000):
    sd=3600000*1.20
if(s==4300000):
    sd=4300000*1.15    
if(s==5000000):
    sd=5000000*1.10    

#salida
print("su cargo es", sd)
print("su nuevo salario es: ", sd)