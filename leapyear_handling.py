check = True
while (check):
    print("Enter your year: ")
    year = input()

    if year.isnumeric() == False:
        check = True
        print("Bad input, try again...")
    else:
        check = False
        year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year!")
        else:
            print(str(year) + " is not a leap year!")
    else:
        print(str(year) + " is a leap year!")
else:
    print(str(year) + " is not a leap year!")
