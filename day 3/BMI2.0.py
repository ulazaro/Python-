# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

print("Whats your height? (Meters)")
hg = float(input())
print("Whats your weight? (kg)")
wg = float(input())

calc = wg / hg ** 2

print(f"Ur BMI is: {round(calc, 2)}")

if calc < 18.5:
    print(" U are underweight")

elif calc >= 18 and calc < 25:
    print("U have a normal weight")

elif calc >= 25 and calc < 30:
    print("U are overweight")

elif calc >= 30 and calc < 35:
    print("U are obese")
else:
    print("U are clinically obese")