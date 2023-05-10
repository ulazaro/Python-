import random

lista = []
quantidade = int(input("Digite o número de pessoas: "))
cont = 0
while cont <  quantidade:
    pessoa = input("Digite o nome da pessoa: ")
    lista.append(pessoa)
    cont += 1  

tamanho = len(lista) - 1
numero = random.randint(0, tamanho)

print(f"Who will pay is: {lista[numero]}")