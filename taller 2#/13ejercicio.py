
"""
entradas
dia--> int -->d
mes--> int -->m
año--> int -->a
Salidas
singno-->str->sig
edad--> int -->edad
"""
#entradas
d =int(input('Digite el numero de dia:'))
m =int(input("Digite el numero de mes:"))
a=int(input("año de nacimiento:"))
#caja negra
edad=2022-a
sig=""
if (d>=21 and m==1) or (d<=19 and m==2):
    sig=('Acuario')
elif (d>=20 and m==2) or (d<=20 and m==3):
    sig=('Piscis')
elif (d>=21 and m==3) or (d<=20 and m==4):
    sig=('Aries')
elif (d>=21 and m==4) or (d<=21 and m==5):
    sig=('Tauro')
elif (d>=22 and m==5) or (d<=21 and m==6):
    sig=('Geminis')
elif (d>=21 and m==6) or (d<=23 and m==7):
    sig=('Cancer')
elif (d>=24 and m==7) or (d<=23 and m==8):
    sig=('Leo')
elif (d>=24 and m==8) or (d<=23 and m==9):
    sig=('Virgo')
elif (d>=24 and m==9) or (d<=23 and m==10):
    sig=('Libra')  
elif (d>=24 and m==10) or (d<=22 and m==11):
    sig=('Escorpio')
elif (d>=23 and m==11) or (d<=21 and m==12):
    sig=('Sagitario')
elif (d>=22 and m==12) or (d<=20 and m==1):
    sig=('Capricornio')
#salida
print("su signo es: ", str(sig))
print("su edad es", int(edad))


