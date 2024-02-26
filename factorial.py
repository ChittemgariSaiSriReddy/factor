num = int(input("Enter a number: "))
factorial = 1
if num < 0:

   print("Sorry, factorial does not exist for negative numbers")

elif num == 0:

    print("The factorial of 0 is 1")

else:
    for i in range(1,num+1):
        factorial = factorial*i
print("The factorial of",num,"is",factorial)

print("****************************************************************************************************")

#factorial of a number using functions

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
num = int(input("Enter a number: "))
if num < 0:

   print("Sorry, factorial does not exist for negative numbers")

elif num == 0:

    print("The factorial of 0 is 1")
else:
    print("Factorial of given number",num ,"is",fact(num))