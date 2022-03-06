estudiantes = {
 "1": {
 "nombre": "Lorea",
 "nota": 8
 },
 "2": {
 "nombre": "Markel",
 "nota": 4.2
 },
 "3": {
 "nombre": "Julen",
 "nota": 6.5
 }
}
k=[]
lista=[]
eslista=3
while True:
    datos=input("Inserte nombre y nota final: ")
    nom_nt=(nom,nt)=datos.split(" ")
    nom=str(nom)
    nt=float(nt)
    lista.append(datos)
    eslista=eslista+1
    if eslista==11:
        break
    for i in lista:
        estudiantes.update({f"{eslista}":{"nombre":nom,"nota":nt}})
    print(estudiantes)

    lista_notas=[]
    for i in range(1,(eslista+1)):
        a=(estudiantes[i]["nota"])
        lista_notas.append(int(a))
    promedio=(sum(lista_notas)/(eslista))
    print("El promedio es de: ", promedio)
    
    
lap=[]
lp=[]
for i in range(1,(eslista+1)):
    if(estudiantes[i]["nota"]<6.0):
        c=(estudiantes[i]["nombre"])
        d=(estudiantes[i]["nota"])
        lp.append(c)
        lp.append(d)
print("los estudiantes que no pasaron son:",lp)        
for i in range(1,(eslista+1)):
    if(estudiantes[i]['nota']>=6.0):
        e=(estudiantes[i]["nombre"])
        f=(estudiantes[i]["nota"])
        lap.append(e)
        lap.append(f)
print("los estudiantes que pasaron son :",lap)