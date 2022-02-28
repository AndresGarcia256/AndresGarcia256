archivo=open('paises.txt','r+', encoding="utf8") 
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M "listo"
"""
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for b in range(a+2,len(i)-1):
    lista.append(i[b])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i[0]=="M"):
    print(i)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U " listo papi"
"""
lista=[]
paises=[]
capitales=[]
for i in archivo:
  a=i.index(":")
  b=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  capitales.append(b)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
for i in capitales:
  if(i[0]=="U"):
    print(i)
"""  

#Cuente e imprima cuantos paises que hay en el archivo " listo"
"""
lista=[]
c=0
for i in archivo:
  lista.append(i)
  a=i.index(":")
  c=c+1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
print(c)
"""
#Busque e imprima la ciudad de Singapur "listo"
"""
lista=[]
ciudad=[]
for i in archivo:   
  a=i.index(":")
  for b in range(a+2,len(i)-1):
    lista.append(i[b])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for p in ciudad:
  if(p=="Singapur"):
    print(p)
"""
#Busque e imprima el pais de Venezuela y su capital "listo"
"""
lista=[]
pais=[]
capital=[]
for i in archivo:
  a=i.index(":")
  b=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  capital.append(b)
  lista=[]
for i in pais:
  if(i=="Venezuela"):
    print(i)
for i in capital:
  if(i=="Caracas"):
    print(i)
"""
  
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
paises=[]
ciudad=[]
for i in archivo:
  lista.append(i)
for i in lista:  
  if(i[0]=="E"):
    paises.append(i)  
for i in paises:
  x=i.index(":")     
  for r in range(x+2,len(i)-1):
    ciudad.append(i[r])
  b = "".join(ciudad)  
  for m in ciudad:
    m="".join(ciudad)
  ciudad=[]
  print(m)
print(len(m)+1)
"""
#Busque e imprima la Capiltal de Colombia
"""
lista=[]
capital=[]
for i in archivo:
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  capital.append(b)
  lista=[]
for i in capital:
  if(i=="Bogotá"):
    print(i)
"""
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México\n"):
    break
  lista=[]   
print(c)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt,
# ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo.
# Utilice un For para cambiar ese Dato
"""
lista=[]
for i in archivo:
  lista.append(i)
lista.remove=("Madagascar: rey julien\n")
lista.insert=(109,"Madagascar: Antananarivo")
print(lista)
"""
#Agregue un país que no esté en la lista 
"""
lista=[]
agregar=[]
for agragar in archivo:
  lista.append(agragar)
  lista.insert("pais")
archivo.close()
"""
