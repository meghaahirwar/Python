a = 10
print(a)

b= 10
print(a, b)
print("a", b)
print(id(a), id(b)) #id() function for finding memory location

c = 20
print(id(a), id(b), id(c)) #if value of variable is different then memory location is also different 

d = "Megha"
print(d)

d1 = "Ahirwar"
print(d1)

#a b = "wrong variable because it's using space in between"
a_b = "it's a right format to creating varible"
print(a_b)   #we can print variable like this
print("a_b")  #this is work as a string not a variable


#@a = 10  #can't use special characters
_a = 10 # only under_score can use in variable


#variable can't start with number like example
#1a = 10 #this is wrong

#camal case variable
myVariableName = "Megha"

#pascal case
MyVariableName = "Priya"

#snake case
my_variable_name = "Lavanya"







#Global variables
name ="Megha"

def my_name():
    global name
    print("My name is", name)
my_name() 

x = str(3)
#y = int("megha")
#print(x, y)
print(type(x))

a = 5
b= 2
print(a//b)