lista = [192, 456, 345, 7, 45, 345, 6, 234]
menor = lista[0]
for n in lista:
    if n < menor: 
        menor = n
print(menor)