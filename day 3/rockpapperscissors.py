import random
# Rock Paper Scissors ASCII Art

print("Welcome to the Rock, Papper Scissors! ")

choose = input("Chosse Rock(R), Papper(P) or Scissor(S): ")
if choose == 'R':
    your_choise = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
if choose == 'P':
    your_choise = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
if choose == 'S':
   your_choise== """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


lista = ['Rock', 'Papper','Scissor']
escolha_maquina = random.randint(0,2)

if escolha_maquina == 0:

    print(f"{your_choise}\nComputer choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

if escolha_maquina == 1:
    print(f"{your_choise}\nComputer choice:")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
if escolha_maquina == 2:
    print(f"{your_choise}\nComputer choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#pedra = 0, papel = 1 e tesoura = 2

if escolha_maquina == 0 and choose == "R":
    print("Draw!")
elif escolha_maquina == 1 and choose == "P":
    print("Draw!")
elif escolha_maquina == 2 and choose == "S":
    print("Draw!") #empates
elif escolha_maquina == 0 and choose == "P":
    print("You Win!")
elif escolha_maquina == 0 and choose == "S":
    print("You Lose!") # casos de vitória e derrota caso a máquina escolha pedra
elif escolha_maquina == 1 and choose == "R":
    print("You Lose!")
elif escolha_maquina == 1 and choose == "S":
    print("You Win!") #casos de vitória ou derrota caso a máquina escolha papel
elif escolha_maquina == 2 and choose == "R":
    print("You Win!")
elif escolha_maquina == 2 and choose == "P":
    print("You Lose!") #casos de vitória ou derrota caso a máquina escolha tesoura
 
else:
    pass