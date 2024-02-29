# Leap Year Checker: Write a program that checks if a year input by the user is a leap year or not.

year=int(input("Enter a Year:"))
# if (year % 400 == 0):                         
    # if we are using symbol / its not giving correct output
if (year % 4 == 0 and year % 100 != 0):
    print("Given Year",year, "is a Leap Year")
else:
    print("Given Year",year, "is not a leap Year")




print("*************************************************************************************************")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
try:
        year = int(input("Enter a year: "))
        if year < 0:
            print("Please enter a valid positive year.")
        elif is_leap_year(year):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
except ValueError:
        print("Please enter a valid integer year.")