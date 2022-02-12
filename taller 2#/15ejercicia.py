
"""
Datos de entrada
hemoglobina-->hmn-->int
edad-->edad-->int
sexo-->sx-->srt
Datos de salida

"""
#entradas
edad=int(input("indique su edad en meses:" ))
sx=int(input("indica tu sexo en femenino como 1 o masculino como 2 : "))
hmn=int(input("nivel de hemoglobina:"))
#caja negra

if(edad>0 and edad<=1) and (hmn>=13 and hmn<=26 ):
    anm="no tiene anemia"
elif(edad>1 and edad<=6) and (hmn>=10 and hmn<=18 ):
    anm="no tiene anemia"
elif(edad>6 and edad<=12) and (hmn>=11 and hmn<=15 ):
    anm="no tiene anemia"
elif(edad>12 and edad<=60) and (hmn>=11.5 and hmn<=15 ):
    anm="no tiene anemia"
elif(edad>60 and edad<=120) and (hmn>=12.6 and hmn<=15.5 ):
    anm="no tiene anemia"
elif(edad>180) and (hmn>=12 and hmn<=16) and (sx==1) :
    anm="no tiene anemia"
elif(edad>180) and (hmn>=14 and hmn<=18 ) and (sx==2) :
    anm="no tiene anemia"
else:
    anm=("tiene anemia")    
#salida
print("",anm)
