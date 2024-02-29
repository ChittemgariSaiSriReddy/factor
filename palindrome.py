#Palindrome Checker: Write a program to check if a word or phrase is a palindrome

def reverse():
     str = ""
     for i in word:
         str = i + str
     return str

word=str(input("Enter a string to check weather it is a palindrome or not : "))
if(reverse()==word):
     print("The Entered String is a Palindrome")
else:
     print("The Entered String is not a Palindrome")


print("***************************************************************************************************")



word=str(input("Enter a string to check weather it is a palindrome or not : "))
pal=word[::-1]
if(word==pal):
     print("The Entered String is a Palindrome")
else:
     print("The Entered String is not a Palindrome")