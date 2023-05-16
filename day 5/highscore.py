#irei utilizar as funções de max e min do python

alunos = int(input("Digite quantos alunos você quer colocar: "))
lista = []

for i in range (0,alunos):
   nota =  int(input("Digite a nota do aluno: "))
   lista.append(nota)
   i += 0

print(f"A maior nota é de {max(lista)}")