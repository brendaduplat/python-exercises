lista = [1, 2, 2, 3, 4, 4, 5]
lista_2 = []
for n in lista:
    if n not in lista_2:
        lista_2.append(n)
print(lista_2)
