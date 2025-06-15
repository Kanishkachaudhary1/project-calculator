# python program to create a simple calculator

# 3 steps to calculate program
# functions for operations
# user input
# print result

#Step-1
# Function to add two numbers
def add(num1,num2):
    return num1 + num2

# Function to subtract two numbers
def sub(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def mul(num1, num2):
    return num1 * num2

#Function to divide two numbers
def div(num1, num2):
    return num1 / num2

# Function to average two numbers
def avg(num1, num2):
    return (num1 + num2)/2

#step-2
print("please select a operations:\n" \
      "1. addition\n"\
      "2. subtract\n"\
      "3. multiply\n"\
      "4. divide\n"\
      "5  average\n")
select =int( input("select a operation from 1,2,3,4,5:"))

number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))

#step-3
if select==1:
    print ("Sum of two numbers is:", add(number1, number2))
elif select==2:
    print ("sub of two numbers is:", sub(number1,number2 ))
elif select==3:
    print ("mul of two numbers is:", mul(number1,number2 ))  
elif select==4:
    print ("div of two numbers is:", div(number1,number2 ))  
elif select==5:
    print ("avg of two numbers is:", avg(number1,number2 )/2)
else:
    print ("invalid operation! please select again!" )   
