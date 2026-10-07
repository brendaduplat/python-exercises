num = int(input("Digite um numero entre 1 e 10: "))

def tabuada(num):
    print(f"Tabuada do {num}:")
    for i in range(11):
        tabuada = num * i
        print(f"{num} x {i} = {tabuada}")

tabuada(num)