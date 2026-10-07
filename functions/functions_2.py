lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
def multiplos_3(lista: list) -> list:
    multiplos =[]
    for i in lista:
        if i % 3 == 0:
            multiplos.append(i)
    return multiplos

print(multiplos_3(lista))