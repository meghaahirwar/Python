# Data Types:
# There are two types of data types in python
# 1. mutable
# 2. immutable
# Definition: mutable data types can change it's state or content but immutable data type can't change anything

# mutable data types: 
#  a) List 
#  b) dictionary
#  c) byte Array

# immutable data types:
#  a)int
#  b)float
#  c)complex
#  d)string
#  e)touple
#  f)set

#-------------------------------------------------------------------
#Number data type
#integer
#float
#complex
print("INTEGER Output: \n")

a = 5
print(a, type(a))

b= 5.5
print(b, type(b))

c = 2 + 5j
print(c, type(c))

#--------------------------------------------------------------

#string data type
#Definition: string is a sequence of characters, special characters and numbers.

print("STRING Output: ")
str = "This is a string"
print(str, type(str))

str0 = '10'   #numners also we can use as a string
print(str0, type(str0))

str1 = """  
    this 
    is 
    a 
    multiline
    string
    """  #for writing multiline string need to use tripal quote
print(str1)

#-------------------------------------------------------------------------------

#List data type
#Definition: List is a ordered sequens of an elements, it is an mutable data type in the python and also most used in python.
# we can perform update , delete operations in the list.  it can store any type of value and it is defined within square[] bracket 

print("LIST Output: ")
list1 = [1, "Megha", 42.3]
print(list1, type(list1))

#update operation
list1[0] = 2
print(list1, type(list1))  #Now list1 will change, list1 = [2, "Megha", 42.3]

list1.remove("Megha")    #if we want to remove any element by using remove() , then here we need to pass that element
print(list1)

list1.append("Priya")   #Append() add an element in the last 
print(list1)

list1.insert(2, "Megha")   #if we add element by using insert then we need to pass index also
print(list1)

list1.insert(6, "sanjay")
print(list1)

list1.insert(1, "sanjay")
print(list1)

list1.pop()   #pop() remove last element from the list
print(list1)

list2 = [1, 2, 3 ,4, 5]
list1.extend(list2)     #we can add two list by using extend()
print(list1)
#---------------------------------------------------------------------------------

#tuple data type
#Definition: tuple is a ordered sequence of an items same as a list, this is immutable data type in python
# we cannot perform update , delete operations in the tuple.  it can store any type of value
#differnce between list and tuple: this is fast as compared to list, we can access tuple quickly and it is defined within paranthesis()
print("TUPLE Output: ")
tuple1 = (1, 2, "Megha", 42.3)
print(tuple1, type(tuple1))

tuple2 = (10)   #it can't keep one value as a tuple, one value it will consider as a int or that type has value
print(tuple2, type(tuple2))

#update operation
#tuple1[0] = 2   #we cannot perform update , delete operation in a tuple
print(tuple1, type(tuple1)) 

#----------------------------------------------------------------------------------------

#Dictionary data type
#Definition: Dictionary data type is an unordered collection of Key-value pairs, dictionary defined within curly-braces{}.
#this is mutable data type.
print("DICTIONARY Output: ")
dictionary = {"Key": "value",
              "Name": "MEgha",
              "age": 23,
              "weight": 43.3}

print(dictionary, type(dictionary))
print(dictionary["Name"])

#------------------------------------------------------------------------

#Set data type
#Definition: A set is an unordered collection of an items and work on unique values, it only takes unique values and can remove duplicate values.
#this is a immutable data type
print("SET Output: ")
Set = {10, 20, 10, "MEgha"}
print(Set, type(Set))   #print only {10, 20, "MEgha"}







#Data Types in the Python

int = 23
string = "Megha Ahirwar"
float = 42.3
bool = True