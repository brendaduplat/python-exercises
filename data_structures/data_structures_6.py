estoque = [
    {"produto": "Notebook", "quantidade": 15, "quantidade_minima": 5},
    {"produto": "Mouse", "quantidade": 42, "quantidade_minima": 10},
    {"produto": "Teclado", "quantidade": 8, "quantidade_minima": 10},
    {"produto": "Monitor", "quantidade": 12, "quantidade_minima": 4},
    {"produto": "Headset", "quantidade": 6, "quantidade_minima": 8},
    {"produto": "Webcam", "quantidade": 18, "quantidade_minima": 5},
    {"produto": "Impressora", "quantidade": 3, "quantidade_minima": 2},
    {"produto": "Cadeira Gamer", "quantidade": 4, "quantidade_minima": 3},
    {"produto": "Mesa Escritório", "quantidade": 2, "quantidade_minima": 2},
    {"produto": "HD Externo", "quantidade": 11, "quantidade_minima": 5},
    {"produto": "SSD 1TB", "quantidade": 7, "quantidade_minima": 6},
    {"produto": "Pendrive 64GB", "quantidade": 25, "quantidade_minima": 10},
    {"produto": "Roteador", "quantidade": 9, "quantidade_minima": 4},
    {"produto": "Switch", "quantidade": 5, "quantidade_minima": 3},
    {"produto": "Cabo HDMI", "quantidade": 30, "quantidade_minima": 15},
    {"produto": "Adaptador USB", "quantidade": 13, "quantidade_minima": 8},
    {"produto": "Fonte ATX", "quantidade": 4, "quantidade_minima": 5},
    {"produto": "Placa de Vídeo", "quantidade": 2, "quantidade_minima": 2},
    {"produto": "Memória RAM 16GB", "quantidade": 14, "quantidade_minima": 6},
    {"produto": "Processador", "quantidade": 5, "quantidade_minima": 3}
]

for item in estoque:
    if item["quantidade"] > item["quantidade_minima"]:
        item["status"] = "Ok"
    else:
        item["status"] = "Alerta"

print(estoque)