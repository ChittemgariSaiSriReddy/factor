# List Element Access: Write a script to access an element in a list based on user input and handle index errors.


my_list = [10, 20, 30, 40, 50]

while True:
    try:
        index = int(input("Enter the index of the element you want to access: "))
        value = my_list[index]
        print("The value at index", index, "is:", value)
        break
    except IndexError:
        print("Error: Index is out of range. Please enter a valid index.")