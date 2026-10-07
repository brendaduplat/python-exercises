frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
dicionario = {}
for n in frutas:
    if n in dicionario:
        dicionario[n] += 1
    else:
        dicionario[n] = 1
print(dicionario)