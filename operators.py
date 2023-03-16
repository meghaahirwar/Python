 #airthetic operators
a = 10
b = 20
print(a + b) #addition operator
print(a - b) #substraction operator
print(a * b) #multiplecation operator
print(a / b) #floting point Division operator

print(a % 3) #modulus operator return reminder 
print(5 ** 2) #exponents operators, it means 5*5 = 25
print(5 **3) #it means 5*5*5 = 125
print(10 / 3) 
print(10 // 3) #floor or integer division operator


#Assignent operators
a = 20            # equal to(=) operator
b = 20
print(a)
 
a += 3            # it means a = a+3
b = b+3
print(a, b)

a -= 6            # it means a= a-3
b = b-6
print(a, b)


#comparison  operators
# == (equal to)
# != (not equal to)
# >  (greater than)
# <  (Less than)
# >= (greater than or equal to)
# <= (less than or equal to)

x = 10
y = 20
print(x == 20)
print(10 == 10)

print(x != y)
print(10 != 10)

print(x > y)
print(x < y)

print(x >= y)
print(x <= y)


#Logical operators
# AND : all condition are true
# OR : any one condition is true
# NOT : not in any condition

a = 10
b = 20
print(a==10 and a<b and a!=b)  #each condition should be true
print(a==10 or a>b or a==b)  #if any one condition is true then it will return true
print (not a==b)   #it is opposite


#Membership operator
# in: return true if value is in the variable
# not in: return true when value is not in specified variable

str = "Python"
print ('P' in str)
print('p' in str) #small letter 'p' is not in str so it will print false
print('n' in str)

list = [10, 20, 30, 40]
print (50 not in list)  #return true because 50 is not in list


#Identify operators
# is: it is like == , return true if both variable is equal
# is not: it is like !=, return true if both variable is not equal to each other

a = 10
b = 10
print(a is b, a == b)
print(a is not b)

x = 10
y = 20
print(x is not y, x != y)
print(a is y)


#Bitwise operators
# AND(&)
# OR(|)
# XOR()

x = 10
y = 8

print(bin(x))   #calculate binary of a particular number by using bin() function
print(bin(y))
print(x&y, bin(x&y)) #1010
print(x|y, bin(x|y)) #1000
print(x^y, bin(x^y)) #10

# 0b1010
# 0b1000
#& 1000=8
#| 1010=10
#^ 10=2

