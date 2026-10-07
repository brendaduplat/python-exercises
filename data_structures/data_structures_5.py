alunos = [
    {"nome": "Ana", "nota": 7},
    {"nome": "Brenda", "nota": 9},
    {"nome": "Carlos", "nota": 5},
    {"nome": "Caio", "nota": 10}
]
comparativa = alunos[0]
for n in alunos:
    if n["nota"] > comparativa["nota"]:
        comparativa = n 
        #se eu crio uma variavel eu preciso atualizar ela. 
print(comparativa)