print("Welcome to the rollercoaster!!")
height = float(input("What is your height in cm? --> "))
age = int(input("Whats ur age? -->"))
value = 0
if height >= 120:
    

    photo = str(input("Do u want a photo? its R$ 3,00: (Y) // (N)"))
    #Verificando se a pessoa quer tirar uma foto
    if photo == 'Y':
        value += 3
    else:
        pass
    #Verificando a idade
    if age > 18 and age <=44 :
        value += 12
        print(f"You will pay R$ {value}")

    elif age <= 12:
        value += 5
        print(f"You will pay R$ {value}")

    elif age > 12 and age <= 18:
        value += 7
        print(f"You will pay {value}")

    elif age >= 45 and age <= 55:
        print(f"You will not pay, can ride for free!(Only photo if incluided R$ {value})")

    else:
        print("You will pay R$ 5,00")

    

else :
    print("U cant")