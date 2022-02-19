
n=int(input("numero entero positivo: "))
d=int(input("divisor: "))
while True:
    if(n>=0):
        n=n-d
        print(n)
    if(n==0):
        break