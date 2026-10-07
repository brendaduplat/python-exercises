lista = [2, 34, 67, 2356, 4, 56, 80]
maior = lista[0]
for num in lista:
    if num > maior:
        maior = num
print(f'O maior numero é {maior}')