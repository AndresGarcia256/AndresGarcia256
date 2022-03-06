usuarios = {
 "iperurena": {
 "nombre": "Iñaki",
 "apellido": "Perurena",
 "password": 123123
 },
 "fmuguruza": {
 "nombre": "Fermín",
 "apellido": "Muguruza",
 "password": 654321
 },
 "aolaizola": {
 "nombre": "Aimar",
 "apellido": "Olaizola",
 "password": 123456
 }
}
contador=1
n=str(input("Inserte su usuario "))
c=int(input("Inserte su contraseña "))
while True:
    if n=="iperurena"in usuarios and c==123123:
        a=(usuarios["iperurena"])
        if(usuarios["iperurena"]["password"]==123123):
            print(a["nombre"])
            print(a["apellido"])
        break
    elif n=="fmuguruza"in usuarios and c==654321:
        b=(usuarios["fmuguruza"])
        if(usuarios["fmuguruza"]["password"]==654321):
            print(b["nombre"])
            print(b["apellido"])
        break
    elif n=="aolaizola"in usuarios and c==123456:
        c=(usuarios["aolaizola"])
        if(usuarios["aolaizola"]["password"]==123456):
            print(c["nombre"])
            print(c["apellido"])
        break
    else:
        n=str(input("Inserte su usuario: "))
        c=int(input("Inserte su contraseña:  "))
        contador=contador +1 
        print("usuario o contraseña incorrecta: ")   
    if contador ==3:
        break