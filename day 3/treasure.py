print("Welcome to the treasure Island")
life = 1
user = str(input("What is ur name stranger? - "))
print(f"Find the treasure or die trying {user}!!")
road = input("U are on a road, turn left or right? (L) or (R)")
if road == "L" or road == 'l':
    print("Okay!")
    river = input("After the road, we arrieved to one river: U can swin or wait one boat - (S) Swim // (W) Wait")
    if river == "W" or river == 'w':
        print ("It's Okay")
        doors = input("Now u finded 3 doors - One Red, One Yellow and One Blue - \nWhat dorr are u will open? - (R) // (Y) // (B): ")
        if doors == 'Y' or doors == 'y':
            print("U FINDED THE TREASURE!!!!!!!!!!!!!!!!!!!! CONGRATULATIONS!!!!!!!!!!! ")
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
*******************************************************************************''')
        else:
            print("Wrong door, you died!")
    
    else:
        print("You drowned!")
    
else:
    print("You fallen into a hole and died!")




    