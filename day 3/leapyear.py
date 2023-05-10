year = int(input("Write a year: "))

if year % 4 != 0:
    print("Its not LEAP")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its LEAP")
        else:
            print("Its not LEAP")
    else:
        print("Its LEAP")
