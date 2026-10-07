notas = [4, 6, 10, 9]
media = sum(notas) / len(notas)
print(media)
if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado.')