produtos = [
    {"nome": "camisa", "preco": 50},
    {"nome": "calça", "preco": 120},
    {"nome": "Sapato", "preco": 200}
]
caros = [n for n in produtos if n["preco"] > 100]
sapato = [n1 for n1 in caros if n1["nome"] == "Sapato"]
print(f'{sapato[0]["nome"]} custa {sapato[0]["preco"]} reais.') # aqui eu estou acessando uma lista de dicionario, entao eu preciso do indicie [0] e a chave ["nome"]