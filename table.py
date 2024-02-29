#Multiplication Table Printer: Write a program that prints multiplication tables for numbers 1 to 10


#using for loop
num=int(input("Enter a Number to print table : "))
print(num ,"Table")
for i in range (1,11):
    res=num*i
    print(num ,"x", i ,"=", res)

print("************************************************************************************************************")

#using while loop
num=int(input("Enter a Number to print table : "))
print(num ,"Table")
i=0
while i<10:
    i+=1
    res=num*i
    print(num ,"x", i ,"=", res)