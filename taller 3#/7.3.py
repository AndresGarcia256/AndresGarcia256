
x=int(input("incremento del valor:"))
m=int(input("valor de la exp:"))
while True:
    if(m==0 and x==0):
       break    
    elif((10<=m<=2**32-1) and (0<x<=3)):
        e=x*m
        print(e)
        break

    
    
