#converting temperatures from fahrenheit to celsius

temp=float(input("Enter the Temperature in Fahrenheit:"))
 
if(temp==-17.78):
    print("Temperature in celsius is ZERO(0)")
else:
    celsius=(temp-32) * 5/9
    print("Given Temperatute in celsius is" , celsius )


#converting temperatures from celsius to fahrenheit
temp=float(input("Enter the Temperature in celsius:"))

if(temp==32):
    print("Temperature in Fahrenheit is ZERO(0)")
else:
    fahrenheit=(temp* 9/5)+32
    print("Given Temperatute in fahrenheit is" , fahrenheit)