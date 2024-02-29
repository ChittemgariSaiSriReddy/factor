# Age Calculator: Develop a program that calculates age from the birth year and handles invalid input or future years

currentyear=int(input("Enter current Year:"))

dob=int(input("Enter your Year of birth:"))

age=currentyear-dob   #formula for calculating the age

print("You are",age,"years old")
