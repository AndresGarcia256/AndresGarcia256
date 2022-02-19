s=int(input("consume licorr(si o no) 1 es si 2 es no:"))
listas=[]
listas.append(s)
a=0
r=0
c=0
t=0
w=0
o=0
ar=0
listaar=[]
listasss=[]
listadad=[]
listamen=[]
listacer=[]
listawhi=[]
listaput=[]
while True:
    if((s==2)):
        print(f"aguardiente {a} \nRON {r} \ncerveza {c} \ntequila {t} \nwhisky {w} \notro {o}")
        print(len(listas))
        print(len(listasss))
        print(sum(listamen))
        print(sum(listaput)/sum(listacer))
        print(len(listawhi)/len(listas))
        break
    elif(s==1):
        edad=int(input("¿cual es tu edad? "))
        listadad.append(edad)
        sexo=str(input("¿cual es tu sexo? 1 para masculino y 2 para femenino: "))
        ar=int(input("1-aguardiente, 2-ron, 3-cerveza, 4-tequila, 5-whisky, 6-otro: "))
        listas.append(ar)
        print("nueva encuesta")
        s=int(input("desea continuar con la investigacion, si es 1, no es 2: "))
        if(ar==1):
            a=a+1
        elif(ar==2):
            r=r+1
        elif(ar==3):
            c=c+1
            listacer.append(c)
            if(ar==3 and edad>0):
                put=edad
                listaput.append(put)
                continue
        elif(ar==4):
            t=t+1   
        elif(ar==5):
            w=w+1
            listawhi.append(w)
        elif(ar==6):
            o=o+1   
        elif(edad>=0):
            listadad.append(edad)
            continue
        elif(edad<=18)and(sexo==2):
            yas=edad+sexo
            listasss.append(yas)
            continue
        elif(20>=edad<=25)and(sexo==1) and (ar!=5):
            men=edad+sexo
            if(ar!=5):
                listamen.append(men)
            continue
