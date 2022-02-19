n=int(input("valor de n"))
k=int(input("valor de k"))
print(n)
while True:
    if(k<n):
        n=n-1
        print(n)
    elif(k==n):
        print(k)
        break
