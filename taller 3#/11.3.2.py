s=str(input("consume licor (si o no):"))
a=0
r=0
c=0
t=0
w=0
o=0
ar=0
men=0
edad=0
sexo=0
yas=0
listas=[]
listaar=[]
listasss=[]
listadad=[]
listamen=[]
listacer=[1]
listawhi=[]
listaput=[]
while True:
    if((s=="no")):
        print(f"aguardiente {a} \nRON {r} \ncerveza {c} \ntequila {t} \nwhisky {w} \notro {o}")
        print(len(listas))
        print(len(listasss))
        print(len(listamen))
        print(sum(listaput)/sum(listacer))
        print(len(listawhi)/len(listas))
        break
    elif(s=="si"):
        edad=int(input("¿cual es tu edad? "))
        listadad.append(edad)
        sexo=int(input("¿cual es tu sexo? 1 para masculino y 2 para femenino: "))
        if(edad<19)and(sexo==2):
            yas=edad
            listasss.append(yas)
        ar=int(input("1-aguardiente, 2-ron, 3-cerveza, 4-tequila, 5-whisky, 6-otro: "))
        listas.append(ar)
        print("nueva encuesta")
        s=str(input("desea continuar con la investigacion, si o no: "))
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
        elif(ar!=5):
            if(19>edad<26)and(sexo==1):
                men=edad
                listamen.append(men)
            
            
            

