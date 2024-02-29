# Input Validation: Create a script that validates user input and uses exception handling to manage non-numeric inputs

while True:
    try:
        num=int(input("Enter a number:"))
        break

    except:
        print("Enter the numeric value")


print("You Entered",num)