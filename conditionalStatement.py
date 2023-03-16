#Conditional statements: conditional statemente is used to decision making
#1) If statement
#2) if else statement
#3) elif

#-----------------------------------------------------------------------------------

#if statemnet: if given condition is true then print output otherwise it not print anything

a = int(input("Enter the value: "))
if a%2 ==0:
    print("This is an even number")
    
#-----------------------------------------------------------------------------------

#if else statement: if given condition is false then also print else part output

a = int(input("Enter the value: "))
if a%2 ==0:
    print("This is an even number")
else:
    print("This is an odd number")
    
#------------------------------------------------------------------------------------

#elif statement: if want to check multiple condition then we can use elif statement

marks = int(input("Enter your marks: "))

if marks > 60:
    print("First Division")
elif marks < 60 and marks > 45:
    print("second division")
elif marks < 45:
    print("Third division")
else:
    print("Fail")
