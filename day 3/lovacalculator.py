name1 = str(input("Write your name: "))
name2 = str(input("Write the name of your love: "))
count1 = 0
count2 = 0

name1_lower = name1.lower()
name2_lower = name2.lower()

for l in name1_lower:
    if l == "t"  or l == "r" or l == 'u' or l == 'e':
        count1 += 1

for n in name2_lower:
    if n == "l"  or n == "o" or n == 'v' or n == 'e':
        count2 += 1


print(f"Tre probability by Love Calculator is {count1}{count2}%")