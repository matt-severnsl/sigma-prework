import datetime


def age_calculator():
    print("Welcome to the age calculator!")
    birth_year = int(input("Please enter the year you were born: "))
    birth_month = int(input("Please enter the month you were born: "))
    birth_day = int(input("Please enter the day you were born: "))

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    # this line isn't used, but is kept for consistency.
    current_day = datetime.date.today().day

    age_in_years = current_year - birth_year

    if current_month < birth_month:
        age_in_years -= 1
    else:
        age_in_years = current_year - birth_year

    print("You are " + str(age_in_years) + " years old.")


age_calculator()
