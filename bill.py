print("Whats the bill value? ")
value = float(input())
people = int(input("How many people will pay this bill?"))
percent = int(input("What is the percent do u wanna pay? 12%, 15% or 20%: "))
percent_float = percent/100
bill_value_percent = round(value * percent_float, 2)
remainder_per_person = round((value - bill_value_percent) / (people -1) , 2)

print(f"You will pay {bill_value_percent}, and the other people will pay {remainder_per_person}")
