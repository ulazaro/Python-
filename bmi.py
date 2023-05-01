print("Whats your height? (Meters)")
hg = float(input())
print("Whats your weight? (kg)")
wg = float(input())

calc = wg / hg ** 2

print(round(calc, 2))