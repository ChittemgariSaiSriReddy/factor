# Number Guessing Game: Implement a number guessing game where the user has to guess a secret number until they get it right.


secreat_number=23
num=int(input("Enter the number less than 100:"))
while (num<=100):
    if (num==secreat_number):
        print("Entered number match with secreat number")
        break
    else:
        print("Entered number doesnot match with secreat number")
        print("try again")
    num=int(input("Enter the number less than 100:"))
    