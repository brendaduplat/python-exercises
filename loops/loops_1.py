numeros = [1, 5, 60, 28, 76, 33] # criar lista de números
soma_pares = 0 # criar variável para acumular a soma dos pares
for num in numeros: # percorrer cada número da lista
    if num % 2 == 0: # verificar se o número é par
        soma_pares += num # somar apenas os números pares
print(soma_pares)