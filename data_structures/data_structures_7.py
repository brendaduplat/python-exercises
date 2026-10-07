alunos = [
    {"nome": "Ana", "nota": 7},
    {"nome": "Brenda", "nota": 9},
    {"nome": "Carlos", "nota": 5}
]
passou = [
    {"nome": aluno["nome"], "nota": aluno["nota"] + 1}
    for aluno in alunos
]
for aluno in passou:
    print(f'Nota atualizada : {aluno}')