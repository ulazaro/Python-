print("Welcome to the timer left (If u live until 90): ")
age = int(input("Whats ur age? "))
age_until_90 = 90 - age
days = age_until_90 * 365
weeks = age_until_90 * 52
months = age_until_90 * 12

print(f"You left {days} days, {weeks} weeks, {months} months.")
