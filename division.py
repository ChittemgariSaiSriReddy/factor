# Division Calculator: Build a division calculator that handles division by zero and other potential errors

try:
    
    dividend = int(input("Enter dividend or Numerator:"))

    divisor  = int(input("Enter divisor or Denominator:"))

    result   = dividend/divisor

    print(result)

except:

    print("Divisor or Denominator value shoud be either than zero")