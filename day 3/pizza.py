print("Welcome, what's the size of the pizza u wanna buy?\nSmall Size ($28) - 'S'\nMedium Size ($32) - 'M'\nLarge Size ($56) - 'L'")
size = input()
bill = 0

if size == 'S':
    bill += 28

elif size == 'M':
    bill += 32

elif size == 'L':
    bill += 56

else:
    print("Invalid choise")

extra_pepperoni = input("Do u wanna extra pepperoni? Y or N: ")
if extra_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do u wanna extra cheese? Y or N: ")
if extra_cheese == 'Y':
    bill += 1

print(f"You should pay ${bill}")

