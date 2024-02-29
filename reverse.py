# printing reverse of string

def reverse(s):
    str = ""
    for i in s:
        str = i + str
        # str = k+G
        # str =e+kg
        
    return str
  
s = str(input("Enter any Sring:")) 
# "Geeksforgeeks"
print("The original string is : ")
print(s)

print("The reversed string(using loops) is : ")
print(reverse(s))