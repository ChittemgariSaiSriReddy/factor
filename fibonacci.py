# Fibonacci Sequence Generator: Develop a program that generates the Fibonacci sequence up to a certain number


fab=int(input("Enter first 2 numbers of sequence:")) #[2,8]
element=int(input("Enter any Number to print fibonacci sequence till that number : "))
while True:
    next_element=fab[-1]+fab[-2]
    # fab.append(next_element)
    # print(fab)
    if(next_element >= element):
      break 
    fab.append(next_element)

print(fab)


#Till the given Index
fab=[0,1]
element=int(input("Enter any Number to print fibonacci sequence till that index value : "))
def fibanacci(element,fab):
   for i in range(2,element):
      next_element=fab[-1]+fab[-2]
      fab.append(next_element)
      return fab[:element]

print(fibanacci(element,fab))
