# Sum of List: Write a function that takes a list of numbers and returns the sum of all the numbers in the list

# def sum_of_list(num):
#     sumoflist=0
#     for n in num:
#        sumoflist+=num
#        return sumoflist

# list=input("Enter a list:")
# numbers_list = [int(x) for x in list.split()]
# print(sum_of_list(list))



def sum_of_list(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

# Take input from the user and convert it into a list of integers
input_str = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(x) for x in input_str.split()]

# Call the function and print the result
print("Sum of the list:", sum_of_list(numbers_list))
