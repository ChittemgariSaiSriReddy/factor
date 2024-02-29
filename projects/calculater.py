# def basic_calculator():
#     while True:
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             operation = input("Enter operation (+, -, *, /): ")

#             if operation == '+':
#                 print(f'Result: {num1} + {num2} = {num1 + num2}')
#             elif operation == '-':
#                 print(f'Result: {num1} - {num2} = {num1 - num2}')
#             elif operation == '*':
#                 print(f'Result: {num1} * {num2} = {num1 * num2}')
#             elif operation == '/':
#                 if num2 == 0:
#                     print("Error! Division by zero.")
#                 else:
#                     print(f'Result: {num1} / {num2} = {num1 / num2}')
#             else:
#                 print("Invalid operation! Please enter a valid operation.")
#         except ValueError:
#             print("Invalid input! Please enter valid numbers.")
#         except Exception as e:
#             print("An error occurred:", e)

#         choice = input("Do you want to perform another calculation? (yes/no): ")
#         if choice.lower() != 'yes':
#             break


# # if __name__ == "__main__":
# basic_calculator()






