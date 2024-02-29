#File Reader: Write a program that reads a file and handles exceptions like File Not Found

try:
    file_name = input("Enter the file name: ")
    a = open(file_name, "r")
    print(a.read())
    a.close()

except IOError:
    print("File Not Found")