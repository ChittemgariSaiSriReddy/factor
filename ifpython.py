# a=235
# b=235 
# if a<b:
#     print("b is greater")
# elif b<a:
#     print("a is greater")
# else:
#     print("both are equal")

# x=10
# y=23



# try:
#   x=10
#   y=23
#   print(x)
#   z=x+y
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")



# for i in range(1,10,1):
#  print(i+1)


# i = 1
# while i < 6:
  
#   if i == 3:
#     break
#   print(i)
#   i += 1



# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
 
# s = "Geeksforgeeks"
 
# print("The original string is : ", end="")
# print(s)
 
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))



# def add(num1: int, num2: int) -> int:
     
# 	"""Add two numbers"""
# 	num3 = num1 + num2

# 	return num3

# # Driver code
# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}.")





# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print(key,"=", value)
 
 
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')




# def add():
#     x = 20

#     def add1():
#         x = 30
#         y = 20
#         return x+y
#     return add1()    


# print(add())




# x=10
# y=20
# z=30
# def add(x):
# 	x=20
# 	def add1():
# 		x=30
# 		y=20
# 	return x+y+z
# 	return add1()
    
# print(add(x))




# x = 10
# y = 20
# z = 30


# def outer():
#     x = 20
#     def inner():
#  	    x = 30
#       y = 40
#       return x+y+z
#     return inner()
  

# print(outer())




# a=10
# b=20
# c=30
# def outer():
#      x=20
#      def inner():
#           x=30
#           y=50
#           return x+y+a
#      return inner()
# print(outer())



def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for uppercase, lowercase, and digits
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    # Return True only if all conditions are met
    return has_upper and has_lower and has_digit

# Get password input from the user
password = input("Enter a password: ")

if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Pasword")
