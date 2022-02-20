lista1=[]
lista2=[]
lista3=[]
e=int(input("cantidad de estudiantes: "))
for i in range(0, e):
    asd=input()
    m=(n, p)=asd.split(" ")
    n=str(n)
    p=int(p)
    lista1.append(p)
    lista2.append(n)
    lista3.append(m)
    ab=sum(lista1)/len(lista1)
    ña = [i for i in lista1 if i>ab]
    ñi=(len(ña)*100)/len(lista1)
    m = [i for i in lista1 if i<ab]
    q=(len(m)*100)/len(lista1)
print(f"el estudiante con mayor puntaje es:", (lista3[lista1.index(max(lista1))]))
print(f"el estudiante con menor puntaje es:", (lista3[lista1.index(min(lista1))]))
print("el mayor puntaje se: ", max(lista1))
print("el menor puntaje es: ", min(lista1))
print("Promedio de puntajes: ", ab)
print(f"porcentaje que etuvo debajo del promedio: {ñi}%")
print(f"porcentaje que estuvo sobre del promedio: {q}%") 