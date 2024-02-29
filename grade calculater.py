# Grade Calculator: Create a script that takes a numerical score and outputs a letter grade (A, B, C, D, F) based on predefined score ranges

marks=int(input("Enter marks out of 100:"))

if(marks>=85):
    print("Grade A")

elif(marks>=75):
    print("Grade B")

elif(marks>=55) & (marks<85):
    print("Grade C")

elif(marks>=45) & (marks<55):
    print("Grade D")

else :
    print("Grade F")