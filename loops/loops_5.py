lista = [0, -34, 56, 78, -2, 0, 34, -16, -68, 57]
positivos = []
negativos = []
zeros = []
for num in lista:
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
    else:
        zeros.append(num)
print('A quantidade de positivos é:', len(positivos))
print('A quantidade de negativos é:', len(negativos))
print('A quantidade de zeros é:', len(zeros))