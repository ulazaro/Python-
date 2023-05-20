'''Creating a password geneartor'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = nr_letters + nr_symbols + nr_numbers
senha = ""


letras_escolhidas = []
simbolos_escolhidos = []
numeros_escolhidos = []
i = 0
for i in range(0 , nr_letters):
     letras_escolhidas.append(random.choice(letters))
    
for i in range(0, nr_numbers):
     numeros_escolhidos.append(random.choice(numbers))

for i in range(0, nr_symbols):
     simbolos_escolhidos.append(random.choice(symbols))

lista_unida = letras_escolhidas + simbolos_escolhidos + numeros_escolhidos

for i in range(0 , len(lista_unida)):

     senha += lista_unida[random.randint(0 , len(lista_unida) - 1)]


print(f"A senha escolhida foi: {senha}")