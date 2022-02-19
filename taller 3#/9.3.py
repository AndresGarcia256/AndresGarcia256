a=0
d=0
g=0
while True:
    numero=int(input(""))
    if(numero==4):
        break

    if(numero==1):
        a=a+1
    elif(numero==2):
        d=d+1
    elif(numero==3):
        g=g+1
    elif(numero==4):
        break
    print(f"MUITO OBRIGADO \nAlcool:,{a} \nGasolina: {g}\nDiesel:{d}")