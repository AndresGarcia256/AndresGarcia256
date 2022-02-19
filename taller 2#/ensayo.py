edad_paciente=int(input("Inserte la edad del paciente en su equivalente de años a meses "))
sexo_paciente=str(input("Inserte su sexo de la siguiente manera , femenino (F) o masculino (M) "))
nivel_hemoglobina=float(input("Inserte cual fue el resultado del nivel de hemoglobina en la sangre "))
sexo= sexo_paciente[0] # Es la posicion del caracter que quiero que tome
esultado=''
if (nivel_hemoglobina>=13 and nivel_hemoglobina<=26) and(edad_paciente>=0 and edad_paciente<=1):
    resultado=(" El resultado es Negativo")
elif(nivel_hemoglobina>=10 and nivel_hemoglobina<=18)and(edad_paciente>1 and edad_paciente<=6):
    resultado=(" El resultado es Negativo")
elif(nivel_hemoglobina>=11 and nivel_hemoglobina<=15)and(edad_paciente>6 and edad_paciente<=12):
    resultado=(" El resultado es Negativo") 
elif (nivel_hemoglobina>=11.5 and nivel_hemoglobina<=15) and (edad_paciente>12 and edad_paciente<=60): # Equivalencia entre 1 año y 5 años en meses 
    resultado=(" El resultado es Negativo")
elif (nivel_hemoglobina>=12.6 and nivel_hemoglobina<=15.5) and (edad_paciente>60 and edad_paciente<=120): # Equivalencia entre 5 años y 10 años en meses 
    resultado=(" El resultado es Negativo")
elif (nivel_hemoglobina>=13 and nivel_hemoglobina<=15.5) and(edad_paciente>120 and edad_paciente<=180): # Equivalencia entre 10 año y 15 años en meses 
    resultado=(" El resultado es Negativo")  
elif (nivel_hemoglobina>=12 and nivel_hemoglobina<=16 ) and(edad_paciente>180 and (sexo=="F")): # Equivalencia de 15 a meses 
    resultado=(" El resultado es Negativo")       
elif (nivel_hemoglobina>=14 and nivel_hemoglobina<=18) and (edad_paciente>180) and (sexo=="M"): # Equivalencia de 15 
    resultado=(" El resultado es Negativo")
else:
    resultado= "El resultado es positivo"
print("",resultado)