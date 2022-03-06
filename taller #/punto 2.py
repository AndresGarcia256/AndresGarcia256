Ejemplo={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5} 
lista=[]
for key  in Ejemplo:
    if key not in lista:
        key=Ejemplo[key]   
        lista.append(key) 
print(set(lista))
    
    


