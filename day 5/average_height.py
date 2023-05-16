qtd = int(input("Bem vindo ao Average Height - Digite quantos estudantes serão analisados: "))
contador = 0 
altura_acumulada=0
for i in range(0,qtd):
    altura = float(input(f"Digite a altura do {contador+1}º estudante em cm: "))
    contador +=1
    altura_acumulada += altura #altura_acumulada soma as alturas

media = altura_acumulada / qtd

print(f"A altura média é de {media} cm")