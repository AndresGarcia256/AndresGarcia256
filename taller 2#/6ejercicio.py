"""
Datos de entrada
A -->int -->a
B -->int -->b
C -->int -->c
D -->int -->d
Datos de salida

"""
#entradas
a=int(input("digite el valor de A:"))
c=int(input("digite el valor de B:"))
b=int(input("digite el valor de C:"))
d=int(input("digite el valor de D:"))

#caja negra
resultado=""
if(c>5):
    c=0
    d=0
    b=b+1
elif(b==9):
    b=1
elif(c<5):
    c=0
    d=0
elif(c==5):
    d=0
print("su numero redondeado es", str(a)+str(b)+str(c)+str(d))
#salida2
