#User defined functions
#Definition: A function is a block of statements, reusable code that is used to perform a single, related action.which can be used repetitively in a program and saves the time of a developer.
#there are three types of user defined functions in python
#1) simple function
#2) function with arguments
#3) return type functions

#1) simple function
def simpleFunction():
  print("Hello trainees!")
simpleFunction()
simpleFunction()
simpleFunction()  #we can call functions many times.

# def sumData():
#   userInput1 = float(input("Enter your first number: "))
#   userInput2 = float(input("Enter your second number: "))
#   print(userInput1 + userInput2)
# sumData()
  

#2) function with arguments: information can be passed to a function as a parameter.
def sum(num1, num2):
  print(num1 + num2)
n1 = 10
n2 = 20
n3 = 30
sum(n1, n2)
m1 = 5
m2 = 5
sum(m1, m2) #we can call functions many times after changing value also

def sum(num1=10, num2 =13):
  print(num1 + num2)
sum()

def sum(num1=10, num2 =13):
  print(num1 + num2)
sum(50, 50)  #it can overrite the given value

def sum(num1, num2 =13):
  print(num1 + num2)
sum(50, 60)   #here, the value of num2 will be overrite by 60

# def sum(num1, num2 =13):
#   print(num1 + num2)
# sum()   #Error because here I am passing only one value

# def sum(num1 = 20, num2):  #Error because I am givinng here two values for one argument
#   print(num1 + num2)
# sum(10)

# def sum(num1 = 20, num2):  #Error 
#   print(num1 + num2)
# sum(, 10)

def sum(num1, num2 =15):
  print(num1 + num2)
sum(10)



#2) function with arguments but without declaring variables inside the functions
def sum(num1, num2):
  print(num1 + num2)
sum(2, 5)

#3) return type functions
#Definitin:  when we dont want to print values but we want to store that operation then we can use return type function
def sumData(ni, n2):
  c = ni + n2
  return c
a = sumData(10, 20)
print(a)

def sumData(ni, n2):
  c = ni + n2
  return c, c * 2   #we can return multiple values in a one function
a = sumData(10, 20)
print(a)

# def calculator():
num1 = float(input("Enter your value 1: "))
num2 = float(input("Enter your value 2: "))
opr = "+", "-", " *", "/" 
  
if opr == "+":
    print(sumData(num1, num2))



