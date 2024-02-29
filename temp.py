def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# def main():
if __name__== "__main__":
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ")

    if unit.upper() == 'F':
        celsius = fahrenheit_to_celsius(temp)
        print(f"{temp} Fahrenheit is equal to {celsius} Celsius.")
    elif unit.upper() == 'C':
        fahrenheit = celsius_to_fahrenheit(temp)
        print(f"{temp} Celsius is equal to {fahrenheit} Fahrenheit.")
    else:
        print("Invalid unit. Please enter 'F' or 'C'.")

# if __name__ == "__main__":
#     main()
